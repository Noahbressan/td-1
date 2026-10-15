"""Client Modbus TCP : lit DI 0 (température haute)."""

from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=5020)
client.connect()

result = client.read_discrete_inputs(address=0, count=1)
if not result.isError():
    print("DI 0 (temp > 22 °C) :", result.bits[0])

client.close()
