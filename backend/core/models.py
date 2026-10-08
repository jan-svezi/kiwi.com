from pydantic import BaseModel, ConfigDict, Field, field_validator


class AirportInfo(BaseModel):
    """Airport metadata resolved from an IATA location code."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    code: str = Field(min_length=3, max_length=3, description="IATA airport code, e.g. PRG.")
    airport_name: str = Field(min_length=1)
    city_name: str = Field(min_length=1)
    country: str = Field(min_length=1)


class FlightSegment(BaseModel):
    """One flight segment (leg) in the decoded boarding-pass payload."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    booking_reference: str = Field(min_length=1, description="PNR / booking reference.")
    airline_code: str = Field(min_length=2, max_length=2, description="Two-character IATA airline code.")
    flight_number: str = Field(min_length=1)
    julian_date: int = Field(ge=1, le=366, description="Day of year of the flight (1–366).")
    cabin_class: str = Field(min_length=1, description="Cabin class, e.g. economy.")
    seat: str = Field(min_length=1, description="Seat number, e.g. 29C.")
    passenger_status: str = Field(min_length=1)
    origin: AirportInfo
    destination: AirportInfo


class DecodedBoardingPass(BaseModel):
    """Decoded boarding-pass payload matching the API JSON contract."""
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    passenger_name: str = Field(min_length=1, description="Passenger name in SURNAME/NAME format.")
    legs: list[FlightSegment] = Field(min_length=1)

    @field_validator("passenger_name")
    @classmethod
    def _validate_passenger_name(cls, value: str) -> str:
        if "/" not in value:
            raise ValueError("passenger_name must use SURNAME/NAME format")
        surname, _, given = value.partition("/")
        if not surname.strip() or not given.strip():
            raise ValueError("passenger_name must use SURNAME/NAME format")
        return value
