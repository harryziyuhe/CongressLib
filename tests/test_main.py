import pytest
from py_congress.main import PyCongress
from py_congress.amendment import Amendment
from py_congress.bill import Bill
from py_congress.committee import Committee
from py_congress.communication import Communication
from py_congress.congress import Congress
from py_congress.member import Member
from py_congress.nomination import Nomination
from py_congress.record import Record
from py_congress.summary import Summary
from py_congress.treaty import Treaty

@pytest.fixture
def client():
    """
    Fixture to create a PyCongress client instance.
    """
    return PyCongress(apikey="test_api_key")

def test_pycongress_initialization(client):
    """
    Test that the PyCongress client initializes correctly with the given API key.
    """
    assert client.apikey == "test_api_key"
    assert client.base_url == "https://api.congress.gov/v3/"

def test_submodule_initialization(client):
    """
    Test that all submodules of PyCongress are initialized correctly.
    """
    assert isinstance(client.amendment, Amendment)
    assert isinstance(client.bill, Bill)
    assert isinstance(client.committee, Committee)
    assert isinstance(client.communication, Communication)
    assert isinstance(client.congress, Congress)
    assert isinstance(client.member, Member)
    assert isinstance(client.nomination, Nomination)
    assert isinstance(client.record, Record)
    assert isinstance(client.summary, Summary)
    assert isinstance(client.treaty, Treaty)
