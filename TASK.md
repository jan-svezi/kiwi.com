# Boarding Pass Parsing

## Task

Create a REST API that parses a boarding pass and serves the decoded data in JSON format.

The boarding pass is a PDF file containing an embedded PDF417 barcode. The barcode encodes the
boarding pass data in the IATA Bar Coded Boarding Pass (BCBP) standard, so parsing means extracting
the barcode from the PDF, decoding it, and decoding the BCBP payload it carries.

An example boarding pass for testing is included in this project at `boarding_pass.pdf` in the
repository root.

The API has two endpoints:

1. `POST /boarding-pass/parse-from-file` — parse an uploaded boarding pass and return the decoded data.
2. `GET /boarding-passes` — list all boarding passes parsed by previous calls to the first endpoint.

### Example: parse a boarding pass

Request:

```bash
curl -X POST \
  'https://checkin-api.examplehost.com/boarding-pass/parse-from-file' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@boarding-pass.pdf;type=application/pdf'
```

Response:

```
200 OK
```

```json
{
  "decoded_bcbp": {
    "passenger_name": "CYPRIAN/MICHAL",
    "legs": [
      {
        "booking_reference": "ZKN85B",
        "airline_code": "FR",
        "flight_number": "7774",
        "julian_date": 105,
        "cabin_class": "economy",
        "seat": "29C",
        "passenger_status": "1",
        "origin": {
          "code": "KSC",
          "airport_name": "Košice International",
          "city_name": "Košice",
          "country": "Slovakia"
        },
        "destination": {
          "code": "PRG",
          "airport_name": "Václav Havel Airport Prague",
          "city_name": "Prague",
          "country": "Czech Republic"
        }
      }
    ]
  }
}
```

The BCBP payload carries only the IATA codes of the origin and destination. To resolve them into
the airport name, city, and country, use the public Locations API:

```bash
curl -X GET 'https://api.skypicker.com/locations/id?id=PRG'
```

### Example: list previously parsed boarding passes

Request:

```bash
curl -X GET \
  'https://checkin-api.examplehost.com/boarding-passes?limit=20&offset=0&passenger_name=CYPRIAN&airline_code=FR' \
  -H 'accept: application/json'
```

Supported query parameters:

| Parameter         | Type    | Description                                                                 |
|-------------------|---------|-----------------------------------------------------------------------------|
| `limit`           | integer | Page size (default `20`).                                                   |
| `offset`          | integer | Number of items to skip (default `0`).                                      |
| `passenger_name`  | string  | Case-insensitive substring match on the passenger name.                     |
| `airline_code`    | string  | Exact match on airline code for any leg (e.g. `FR`).                        |

Response:

```
200 OK
```

```json
{
  "items": [
    {
      "id": "b7d1f0c2-9a3e-4f11-8c0d-2b5e6a7c9d10",
      "parsed_at": "2026-08-10T09:14:22Z",
      "decoded_bcbp": { "... same structure as above ..." }
    }
  ],
  "total": 1,
  "limit": 20,
  "offset": 0
}
```

This endpoint returns boarding passes parsed so far, newest first, paginated, and optionally
filtered by `passenger_name` and/or `airline_code`. When both filters are provided, results must
match all of them. `total` reflects the number of items matching the applied filters.

## Requirements

We want you to demonstrate your best skills. Imagine you are writing an MVP that is ready for
production use, following best coding practices. Write your solution in Python 3. You may use any
publicly available libraries and APIs.

- Ensure proper test coverage.
- Create API documentation, for example OpenAPI 3.0.
- Include a `README.md` with a description and instructions on how to run and test the application.

If you have any ideas on how to make it even better, feel free to include them.

Using an agentic development tool such as Claude Code, Cursor, or Codex is encouraged — we use them
daily. Just make sure you understand and stand behind every line of the result, as we will discuss
the solution with you.

## Submission

Once you are done, create a private repository with your solution on GitHub and add
[@mcyprian](https://github.com/mcyprian) and [@rlapar](https://github.com/rlapar) as contributors.