# tests/test_linked_list.py
# Pruebas base escritas por el docente.
# CADA EQUIPO agregará sus propias pruebas en este archivo
# desde su rama — esto generará merge conflicts intencionales.

import pytest
from src.linked_list import LinkedList, Node


# ------------------------------------------------------------------ #
# Pruebas del docente — __str__ y __len__                             #
# ------------------------------------------------------------------ #

def test_lista_vacia_str():
    ll = LinkedList()
    assert str(ll) == "Lista vacía"


def test_lista_vacia_len():
    ll = LinkedList()
    assert len(ll) == 0


def test_node_repr():
    n = Node(42)
    assert repr(n) == "Node(42)"


# ------------------------------------------------------------------ #
# Pruebas Equipo A - append
# ------------------------------------------------------------------ #

def test_append_lista_vacia():
    ll = LinkedList()

    ll.append(10)

    assert ll.head.data == 10
    assert len(ll) == 1


def test_append_varios_elementos():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)

    assert str(ll) == "10 -> 20 -> 30"
    assert len(ll) == 3