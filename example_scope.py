SERVICE_RATE = 0.08

def service_charge(subtotal):
  # SERVICE_RATE = SERVICE_RATE + subtotal
    charge = subtotal * SERVICE_RATE
    return charge

def another_function():
    # SERVICE_RATE is available here.
    # charge is not: it belongs only to service_charge.
    pass

print(service_charge(5))