# validaBandeiraCDC

## Project Overview

**validaBandeiraCDC** is a Python 3.8.20 web service that exposes a REST API to validate credit card numbers and identify their flag (brand), such as Visa, Mastercard, Diners International, and more. The service checks the card number against known patterns and lengths for each flag and returns a JSON response indicating the result.

## How the Program Works

- The API exposes a single endpoint:  
  `GET /validateFlag/{creditCardNumber}`
- When a request is made, the service checks the number against validation rules for each supported flag.
- The response includes:
  - The card number
  - Whether the number is valid for a known flag
  - A message indicating the flag or the reason for invalidity

## How to Run

1. **Install dependencies:**
   ```sh
   pip install fastapi uvicorn
   ```

2. **Start the server:**
   ```sh
   uvicorn webServer:app --reload --port 3000
   ```

3. **Run tests:**
   ```sh
   pip install pytest
   pytest test.py
   ```

## Example Requests and Responses

### Visa (Valid)
```sh
curl --location 'http://127.0.0.1:3000/validateFlag/4234567890123456'
```
Response:
```json
{
    "cardNumber": "4234567890123456",
    "isValid": true,
    "message": "credit card flag: Visa"
}
```

### Mastercard (Valid)
```sh
curl --location 'http://127.0.0.1:3000/validateFlag/2234567890123456'
```
Response:
```json
{
    "cardNumber": "2234567890123456",
    "isValid": true,
    "message": "credit card flag: Mastercard"
}
```

### Diners International (Valid)
```sh
curl --location 'http://127.0.0.1:3000/validateFlag/38410078901234'
```
Response:
```json
{
    "cardNumber": "38410078901234",
    "isValid": true,
    "message": "credit card flag: Diners International"
}
```

### Inexistent Flag (Invalid)
```sh
curl --location 'http://127.0.0.1:3000/validateFlag/3841007890123456'
```
Response:
```json
{
    "cardNumber": "3841007890123456",
    "isValid": false,
    "message": "Inexistent credit card flag"
}
```

## Test Results

```
================================================================= test session starts =================================================================
platform linux -- Python 3.12.7, pytest-7.4.4, pluggy-1.0.0
rootdir: /home/portilloga/work/workspace/github/dio/validaBandeiraCDC
plugins: anyio-4.2.0
collected 4 items                                                                                                                                     

test.py ....                                                                                                                                    [100%]
```

---

**validaBandeiraCDC** makes it easy to validate and identify credit card flags via a simple REST API.