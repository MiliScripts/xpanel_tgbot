def convert_mb_to_gb(amount_mb):
    try:

        if amount_mb < 1024:
            return f"{amount_mb} ᴹᴮ​"
        elif amount_mb < 1024 * 1000:
            amount_gb = amount_mb / 1024
            return f"{round(amount_gb)} ᴳᴮ​"
        else:
            return "♾"
    except:
         return "♾"   
