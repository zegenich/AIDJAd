from src.constants import BookingData
from models.booking import CreateBookingResponse
from conftest import created_booking

def test_create_booking(created_booking):
    try:
        print(created_booking)
        parsed = CreateBookingResponse(**created_booking)
    except Exception as e:
        raise AssertionError(f"NE SOOTVETSTVUET: {e}")

    assert parsed.booking.bookingdates.checkin == "2018-01-01"

    assert created_booking['booking']['firstname'] == BookingData.FIRSTNAME.value, f'Некорректное имя\nПришло: {created_booking}\nОжидалось: {BookingData.FIRSTNAME}'
    assert created_booking['booking']['lastname'] == BookingData.LASTNAME.value, f'Некорректная фамилия\nПришло: {created_booking}\nОжидалось: {BookingData.LASTNAME}'

#def test_update_booking():
