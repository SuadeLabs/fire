import os
from pyspark.sql.types import StructType, \
    StructField, StringType, DoubleType, \
    IntegerType, BooleanType, DateType, TimestampType, ArrayType
import pkg_resources
import json


def load_json(json_file):
    if not os.path.exists(json_file):
        raise Exception("Could not find file {}".format(json_file))
    with open(json_file) as f:
        return json.loads(f.read())


def extract_constraints(schema: StructType, parent: str = None):
    constraints = []
    fields = schema.fields
    for field in fields:
        if parent:
            sql_name = "{}.`{}`".format(parent, field.name)
        else:
            sql_name = "`{}`".format(field.name)
        for exp in field.metadata['constraints']:
            constraints.append(exp.format(sql_name))
        if isinstance(field.dataType, StructType):
            extract_constraints(field.dataType, sql_name)
    return constraints


class FireEntity:

    def __init__(self, schema, constraints):
        self.schema = schema
        self.constraints = constraints


class FireModel:

    def __init__(self, fire_directory=None):
        if not fire_directory:
            fire_directory = pkg_resources.resource_filename(
                self.__module__,
                'data/'
            )
        self.fire_directory = fire_directory

    def __get_array_type(self, tpe, fmt, prp):
        if tpe == "object":
            nested_prp = prp['properties']
            nested_fields = nested_prp.keys()
            nested_required = set(prp['required'])
            nested_structs = []
            for nested_field in nested_fields:
                nested_field_nullable = nested_field not in nested_required
                nested_property = nested_prp[nested_field]
                nested_struct = self.__process_property(
                    nested_field,
                    nested_field_nullable,
                    nested_property,
                    None
                )
                nested_structs.append(nested_struct)
            return StructType(nested_structs)
        elif tpe == "number":
            return DoubleType()
        elif tpe == "integer":
            return IntegerType()
        elif tpe == "boolean":
            return BooleanType()
        elif tpe == "string":
            if not fmt:
                return StringType()
            elif fmt == "date":
                return DateType()
            elif fmt == "date-time":
                return TimestampType()
        raise Exception("Unsupported type {}".format(tpe))

    '''
    Converting a FIRE field into a Spark type
    Simple mapping exercise for atomic types (number, string, etc),
    this process becomes complex for nested entities
    For entities of type object, we recursively parse object
    and map their respective types into StructTypes
    For list, we recursively call that function to extract entity types
    '''
    def __process_property_type(self, name, tpe, nullable, fmt, prp, dsc):

        if tpe == "object":
            # Nested field, we must read its underlying properties
            # Return a complex struct type
            struct = StructType(self.__load_object(prp))
            constraints = self.__validate(nullable)
            return StructField(
                name,
                struct,
                nullable,
                metadata={"desc": 'dsc', "constraints": constraints}
            )

        if tpe == "array":
            # Array type, we need to read its underlying properties
            # Recursive call
            nested_prp = prp['items']
            nested_tpe = nested_prp['type']
            nested_fmt = nested_prp.get('format', None)
            struct = ArrayType(
                self.__get_array_type(nested_tpe, nested_fmt, nested_prp)
            )
            constraints = self.__validate_arrays(prp, nullable)
            return StructField(
                name,
                struct,
                nullable,
                metadata={"desc": 'dsc', "constraints": constraints}
            )

        if tpe == "number":
            constraints = self.__validate_numbers(prp, nullable)
            return StructField(
                name,
                DoubleType(),
                nullable,
                metadata={"desc": 'dsc', "constraints": constraints}
            )

        if tpe == "integer":
            constraints = self.__validate_numbers(prp, nullable)
            return StructField(
                name,
                IntegerType(),
                nullable,
                metadata={"desc": 'dsc', "constraints": constraints}
            )

        if tpe == "boolean":
            constraints = self.__validate(nullable)
            return StructField(
                name,
                BooleanType(),
                nullable,
                metadata={"desc": 'dsc', "constraints": constraints}
            )

        if tpe == "string":
            if not fmt:
                constraints = self.__validate_strings(prp, nullable)
                return StructField(
                    name,
                    StringType(),
                    nullable,
                    metadata={"desc": 'dsc', "constraints": constraints}
                )

            if fmt == "date-time":
                constraints = self.__validate_dates(prp, nullable)
                return StructField(
                    name,
                    TimestampType(),
                    nullable,
                    metadata={"desc": 'dsc', "constraints": constraints}
                )

            if fmt == "date":
                constraints = self.__validate_dates(prp, nullable)
                return StructField(
                    name,
                    DateType(),
                    nullable,
                    metadata={"desc": 'dsc', "constraints": constraints}
                )

        raise Exception(
            "Unsupported type {} for field {}".format(tpe, name)
        )

    def __validate_strings(self, prp, nullable):
        constraints = self.__validate(nullable)
        minimum = prp.get('minLength', None)
        maximum = prp.get('maxLength', None)
        enum = prp.get('enum', None)

        if enum:
            enums = ','.join(["'{}'".format(e) for e in enum])
            exp = "{{0}} IS NULL OR {{0}} IN ({})".format(enums)
            constraints.append(exp)

        if minimum and maximum:
            exp = "{{0}} IS NULL OR LENGTH({{0}}) IS BETWEEN {} AND {}".\
                format(int(minimum), int(maximum))
            constraints.append(exp)
        elif minimum:
            exp = "{{0}} IS NULL OR LENGTH({{0}}) >= {}".\
                format(int(minimum))
            constraints.append(exp)
        elif maximum:
            exp = "{{0}} IS NULL OR LENGTH({{0}}) <= {}".\
                format(int(maximum))
            constraints.append(exp)
        return constraints

    def __validate_dates(self, prp, nullable):
        constraints = self.__validate(nullable)
        minimum = prp.get('minimum', None)
        maximum = prp.get('maximum', None)
        if minimum and maximum:
            exp = "{{0}} IS NULL OR {{0}} IS BETWEEN '{}' AND '{}'".\
                format(str(minimum), str(maximum))
            constraints.append(exp)
        elif minimum:
            exp = "{{0}} IS NULL OR {{0}} >= '{}'".\
                format(str(minimum))
            constraints.append(exp)
        elif maximum:
            exp = "{{0}} IS NULL OR {{0}} <= '{}'".\
                format(str(maximum))
            constraints.append(exp)
        return constraints

    def __validate_numbers(self, prp, nullable):
        constraints = self.__validate(nullable)
        minimum = prp.get('minimum', None)
        maximum = prp.get('maximum', None)
        if minimum and maximum:
            exp = "{{0}} IS NULL OR {{0}} IS BETWEEN {} AND {}".\
                format(float(minimum), float(maximum))
            constraints.append(exp)
        elif minimum:
            exp = "{{0}} IS NULL OR {{0}} >= {}".\
                format(float(minimum))
            constraints.append(exp)
        elif maximum:
            exp = "{{0}} IS NULL OR {{0}} <= {}".\
                format(float(maximum))
            constraints.append(exp)
        return constraints

    def __validate_arrays(self, prp, nullable):
        constraints = self.__validate(nullable)
        # we cannot validate the integrity of each field
        # without exploding array or running complex UDFs
        # we simply check for array size for now
        minimum = prp.get('minItems', None)
        maximum = prp.get('maxItems', None)
        if minimum and maximum:
            exp = "{{0}} IS NULL OR SIZE({{0}}) IS BETWEEN {} AND {}"\
                .format(float(minimum), float(maximum))
            constraints.append(exp)
        elif minimum:
            exp = "{{0}} IS NULL OR SIZE({{0}}) >= {}"\
                .format(float(minimum))
            constraints.append(exp)
        elif maximum:
            exp = "{{0}} IS NULL OR SIZE({{0}}) <= {}"\
                .format(float(maximum))
            constraints.append(exp)
        return constraints

    @staticmethod
    def __validate(nullable):
        constraints = []
        if not nullable:
            exp = "{0} IS NOT NULL"
            constraints.append(exp)
        return constraints

    '''
    Process a fire property (i.e. a field) given a name and a property object
    A field may be a reference to a common object such as currency code,
    so recursive call may be required
    We look at field description
    '''
    def __process_property(self, name, nullable, prp, parent_dsc):

        dsc = prp.get('description', None)
        if parent_dsc:
            # we prefer entity specific description if any rather than generic
            # parent takes precedence
            dsc = parent_dsc

        tpe = prp.get('type', None)
        fmt = prp.get('format', None)
        ref = prp.get('$ref', None)

        # processing referenced property
        if ref:

            # retrieve the name of the Json file and
            # the name of the entity to load
            ref_object = ref.split('/')[-1]
            ref_json = ref.split('#')[0].split('/')[-1]

            # parsing json
            ref_json_file = os.path.join(self.fire_directory, ref_json)
            ref_json_model = load_json(ref_json_file)
            if ref_object not in ref_json_model.keys():
                raise Exception(
                    "Referencing non existing property {}".format(ref_object)
                )

            # processing inline property
            ref_property = ref_json_model[ref_object]
            return self.__process_property(name, nullable, ref_property, dsc)

        # processing property
        struct = self.__process_property_type(
            name,
            tpe,
            nullable,
            fmt,
            prp,
            dsc
        )
        return struct

    '''
    Some entities may be built as a supertype to other entities
    Example: A customer is a supertype to a person entity
    We load that entire referenced entity as we would
    be loading any object, parsing json file into spark schema
    '''
    def __load_reference(self, ref):
        ref_object = ref.split('/')[-1]
        ref_json_file = os.path.join(self.fire_directory, ref_object)
        ref_json_model = load_json(ref_json_file)
        return self.__load_object(ref_json_model)

    '''
    Core business logic, we process a given entity from a json object
    An entity contains metadata (e.g. description),
    required field definition and property value
    We extract each property, map them to their spark
    type and return the spark schema for that given entity
    '''
    def __load_object(self, model):
        required = model['required']
        fields = model['properties']
        schema = []

        # Processing fields
        for field in fields.keys():
            prp = fields[field]
            nullable = field not in required
            struct = self.__process_property(field, nullable, prp, None)
            schema.append(struct)

        # Adding referenced entities
        if "allOf" in model.keys():
            for ref in model['allOf']:
                schema.extend(self.__load_reference(ref['$ref']))

        return schema

    '''
    Entry point, given a name of an entity,
    we access and parse underlying json object
    We retrieve all fields, referenced entities,
    metadata as a spark schema
    '''
    def load(self, model):
        json_file = os.path.join(self.fire_directory, "{}.json".format(model))
        json_model = load_json(json_file)
        tpe = json_model.get('type', None)
        if not tpe or tpe != "object":
            raise Exception("Can only process entities of type object")

        struct = self.__load_object(json_model)
        schema = StructType(struct)
        constraints = extract_constraints(schema)
        return FireEntity(schema, constraints)
