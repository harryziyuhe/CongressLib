import pytest
from congresssdk.main import PyCongress
from congresssdk.amendment import Amendment
from congresssdk.bill import Bill
from congresssdk.committee import Committee
from congresssdk.communication import Communication
from congresssdk.congress import Congress
from congresssdk.member import Member
from congresssdk.nomination import Nomination
from congresssdk.record import Record
from congresssdk.summary import Summary
from congresssdk.treaty import Treaty

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
