import requests
from bitcoinaddress import Wallet

# Get current btc value in usd
URL_COINBASE = "https://api.coinbase.com/v2/prices/spot?currency=USD"
request_coinbase = requests.get(url=URL_COINBASE)
data_coinbase = request_coinbase.json()
BTC_VALUE_USD = int(float(data_coinbase["data"]["amount"]))

def scanAddress(address):
    #Get wallet balance info
    print(f"Scanning address: {address}...")
    URL = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'
    request = requests.get(url=URL)
    data = request.json()

    #Some simple calculations
    if "error" in data:
        print(f"Invalid address: {address}")
        pass
    else:
        balance = data["balance"] / 100000000
        balance_USD = round(balance * BTC_VALUE_USD)
        total_received = data["total_received"] / 100000000
        total_received_USD = round(total_received * BTC_VALUE_USD)
        total_sent = data["total_sent"] / 100000000
        total_sent_USD = round(total_sent * BTC_VALUE_USD)

        if balance != 0:
            print(">-----------------------------------<")
            print(f"Found address: {address} with:")
            print(f"  Balance: {balance} BTC (${balance_USD})")
            print(f"   * Total Sent: {total_sent} BTC (${total_sent_USD})")
            print(f"   * Total Received: {total_received} BTC (${total_received_USD})")
            print(">-----------------------------------<")
        else:
            print("Balance is 0...")



def start():
    amount = int(input("How many wallets should we scan?"))
    while amount != 0:
        amount = amount-1
        wallet = Wallet()
        scanAddress(wallet.address.mainnet.pubaddrbc1_P2WPKH)



start()