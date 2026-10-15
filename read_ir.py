"""Client Modbus TCP : lit IR 0 (température x10)."""

from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=5020)
client.connect()

result = client.read_input_registers(address=0, count=1)
if not result.isError():
    valeur = result.registers[0]
    print("IR 0 :", valeur, "->", valeur / 10, "°C")

client.close()
