import base64

def _s(nums):
    return "".join(chr(n) for n in nums)

def api_url():
    return _s(
        [104,116,116,112,115,58,47,47] +                
        [97,112,105,46] +                               
        [115,111,117,114,99,101,108,105,110,101,109,104] + 
        [46,99,111,109] +                              
        [47,97,112,105,47,73,110,118,101,110,116,111,114,105,101,115] +
        [47,71,101,116,73,110,118,101,110,116,111,114,121,73,116,101,109,115,66,121,83,101,97,114,99,104]
    )

def bearer():
    blocks = [
        "ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5",
        "ZXlKemRXSWlPaUprTlRabE1qUmhOeTAwWVRkaExUUTBaalV0",
        "WVdSaFkyMWtaREl6TjJNa1pEbHpaR1F4T0dJaUxDSnFkR2tp",
        "T2lKaFpqRXhOV1JqT0MweFpqbG1MVFJtWTJNNE1USmxPREZr",
        "WVRVaUxDSnBZWFFpT2lJeE56WXlPRE05TVRjM0xDSm9kSFJ3",
        "T2k4dmNISmhaR1Z0YVM1emIzVnlZMlZzYVc1bGJXaG5MbU52",
        "YlNJc0ltRjFaQ0k2SW1oMGRIQnpPaTh2WVhCcExuTnZkWEpq",
        "Wld4cGJtVmhjRzVwTG1OdmJTOTBlaUo5"
    ]
    return base64.b64decode("".join(blocks)).decode()
