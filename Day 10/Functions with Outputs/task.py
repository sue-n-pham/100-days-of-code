def format_name(f_name, l_name):
    formatted_f = f_name.title()
    formatted_l = l_name.title()
    return f"{formatted_f} {formatted_l}"

format_str = format_name("peRCy", "jACksON") # save output into variable
print(format_str)
