# CongressLib

CongressLib is a Python client library for interacting with the Congress.gov API. It provides a simple and intuitive interface for retrieving legislative data such as bills, amendments, treaties, committee activities, congressional records, and more. This library is designed for researchers, developers, and anyone interested in programmatically accessing Congress.gov data.

---

## Features

- Retrieve lists and detailed information about:
  - Bills
  - Amendments
  - Committees
  - Communications
  - Congressional records (daily and bound)
  - Members of Congress
  - Nominations
  - Summaries
  - Treaties
- Easily handle API authentication with your Congress.gov API key.
- Modular design for extensibility and maintainability.

---

## Installation

Install the package using pip:

```bash
pip install CongressLib
```

Or, clone the repository and install it manually:

```bash
git clone https://github.com/harryziyuhe/CongressLib.git
cd CongressLib
pip install .
```

---

## Getting Started

### Prerequisites

1. **Congress.gov API Key:** You need an API key from [Congress.gov Developer Hub](https://developer.congress.gov/).
2. Python version 3.8 or higher.

### Setup

Store your API key in an environment file (`.env`):

```
apikey=your_congress_api_key
```

### Example Usage

```python
from congresslib import PyCongress

# Initialize the client
client = PyCongress(apikey="your_api_key")

# Retrieve a list of bills
bills = client.bill.get_bill_list(congress=117, limit=5)
print(bills)

# Get detailed information about a specific treaty
treaty = client.treaty.get_treaty(congress=117, number=1)
print(treaty)

# Fetch amendments for a specific bill
amendments = client.amendment.get_amendment_list(congress=117, type="h", limit=10)
print(amendments)
```

## Available Functions

### Bill
- `get_bill_list`: Retrieve a list of bills based on filters like Congress number, type, and date range.
- `get_bill`: Get detailed information about a specific bill.
- `get_bill_actions`: Retrieve a list of actions on a specific bill.
- `get_bill_amendments`: Get amendments related to a specific bill.
- `get_bill_committees`: Retrieve committees associated with a bill.
- `get_bill_cosponsors`: Retrieve cosponsors of a specific bill.
- `get_bill_relatedbills`: Get related bills.
- `get_bill_subjects`: Get legislative subjects related to a bill.
- `get_bill_summaries`: Get summaries for a specific bill.
- `get_bill_text`: Retrieve text versions of a bill.
- `get_bill_titles`: Retrieve titles of a specific bill.
- `get_law_list`: Retrieve a list of laws.
- `get_law`: Retrieve detailed information about a specific law.

### Amendment
- `get_amendment_list`: Retrieve a list of amendments.
- `get_amendment`: Get detailed information about a specific amendment.
- `get_amendment_actions`: Retrieve a list of actions on a specific amendment.
- `get_amendment_cosponsors`: Retrieve cosponsors for a specific amendment.
- `get_amendment_amendments`: Retrieve amendments to a specific amendment.
- `get_amendment_text`: Retrieve text versions of an amendment (117th Congress onwards).

### Committee
- `get_committee_list`: Retrieve a list of congressional committees.
- `get_committee`: Get detailed information about a specific committee.
- `get_committee_bills`: Retrieve bills associated with a committee.
- `get_committee_reports`: Retrieve reports associated with a committee.
- `get_committee_nominations`: Retrieve nominations associated with a committee.
- `get_committee_communications`: Retrieve communications associated with a committee.

### Communication
- `get_communication_list`: Retrieve a list of communications for a chamber (House or Senate).
- `get_communication`: Get detailed information about a specific communication.
- `get_requirement_list`: Retrieve a list of House requirements.
- `get_requirement`: Get detailed information about a specific House requirement.
- `get_requirement_communications`: Retrieve communications matching a House requirement.

### Congress
- `get_congress_list`: Retrieve a list of congresses and congressional sessions.
- `get_congress`: Get detailed information about a specific Congress.

### Member
- `get_member_list`: Retrieve a list of congressional members.
- `get_member`: Get detailed information about a specific member.
- `get_sponsored_legislation`: Retrieve legislation sponsored by a member.
- `get_cosponsored_legislation`: Retrieve legislation cosponsored by a member.

### Nomination
- `get_nomination_list`: Retrieve a list of nominations received from the President.
- `get_nomination`: Get detailed information about a specific nomination.
- `get_nominees`: Retrieve a list of nominees for a position within a nomination.
- `get_nomination_actions`: Retrieve actions related to a nomination.
- `get_nomination_committees`: Retrieve committees associated with a nomination.
- `get_nomination_hearings`: Retrieve hearings associated with a nomination.

### Record
- `get_record_list`: Retrieve a list of congressional record issues.
- `get_daily_record_list`: Retrieve daily congressional record issues.
- `get_daily_record`: Retrieve a specific daily congressional record issue.
- `get_daily_record_articles`: Retrieve articles from a daily congressional record issue.
- `get_bound_record_list`: Retrieve a list of bound congressional records.

### Summary
- `get_summary_list`: Retrieve a list of summaries based on filters like Congress number, type, and date range.

### Treaty
- `get_treaty_list`: Retrieve a list of treaties.
- `get_treaty`: Get detailed information about a specific treaty.
- `get_treaty_actions`: Retrieve actions related to a treaty.
- `get_treaty_committees`: Retrieve committees associated with a treaty.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Congress.gov Developer Hub](https://developer.congress.gov/) for providing API access.

---

## Contact

For questions or feedback, feel free to reach out:

- **GitHub Issues:** [Issues Page](https://github.com/harryziyuhe/py-congress/issues)
