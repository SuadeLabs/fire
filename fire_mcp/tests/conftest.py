from __future__ import annotations

import socket

import pytest


@pytest.fixture
def no_network(monkeypatch):
    """Fail loudly if anything under test tries to open a real socket."""

    def _blocked(*args, **kwargs):
        raise AssertionError("network access attempted during offline ref resolution")

    monkeypatch.setattr(socket, "socket", _blocked)
    monkeypatch.setattr(socket, "create_connection", _blocked)
