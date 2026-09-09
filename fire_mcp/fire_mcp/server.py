"""Entry point: wires up the FIRE MCPServer and runs it (stdio by default)."""

from __future__ import annotations

from mcp.server import MCPServer

from . import resources, tools

mcp = MCPServer("fire")
resources.register(mcp)
tools.register(mcp)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
