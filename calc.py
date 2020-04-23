
print("""
Welcome to this simple sourdough calculator!
Enter the menu items for what you want this script to do.

1) Standard recipes for making bread.
2) Calculate number of loafes you can make based on your avaiable amount of flour.
3) Bakers percentages


""")

choice = input("Enter (1/2/3):  ")

if choice == '1':
    print("""
This is a standard recipe from alexandracooks.com. 
See the full guide here; https://alexandracooks.com/2017/10/24/artisan-sourdough-made-simple-sourdough-bread-demystified-a-beginners-guide-to-sourdough-baking/

    """)
    loafs = int(input("Enter number of loafs you want to bake:  "))
    if loafs > 0:
        flour = (453.5 * loafs)
        water = (345.5 * loafs)
        salt = (9 * loafs)
        levain = (92 * loafs)
        sds = (18.5 * loafs)
        sds_flour = (37 * loafs)
        sds_water = (37 * loafs)
        bread_total = (flour + water + salt + levain)
        print(f"""
This dough devides in to {loafs} equal sized loafs.

The levain contains the following:

Sourdough starter: {sds}g
Roomtemp water: {sds_water}g
Flour: {sds_flour}g

The autolyse bread dough contains the following:

Flour: {flour}g
Salt: {salt}g
Water: {water}g

Adding the levain ({levain}g) to the dough it should weigh {bread_total}g.
        """)
    else:
        print("Please enter a number larger than zero")
elif choice == '2':
    print("""
This feature calculates the number of loafs you can bake based on the amount of flour you have available.
The bakers percentages used in the following recipe is based on alexandracooks.com ratios.

    """)
    flouramount = int(input("Enter the amount of flour in grams (one cup of AP flour is ca 128 grams): "))
    nuoflo = int((flouramount // 453.5))
    
    flour_calc = (453.5 * nuoflo)
    water_calc = (345.5 * nuoflo)
    salt_calc = (9 * nuoflo)
    levain_calc = (92 * nuoflo)
    sds_calc = (18.5 * nuoflo)
    sds_flour_calc = (37 * nuoflo)
    sds_water_calc = (37 * nuoflo)

    bread_total_calc = (flour_calc + water_calc + salt_calc + levain_calc)
    if flouramount > 0:
        print(f"""

{flouramount} grams of flour devides in to {nuoflo} equal sized loafs.

The levain contains the following:

Sourdough starter: {sds_calc}g
Roomtemp water: {sds_water_calc}g
Flour: {sds_flour_calc}g

The autolyse bread dough contains the following:

Flour: {flour_calc}g
Salt: {salt_calc}g
Water: {water_calc}g

Adding the levain ({levain_calc}g) to the dough it should weigh {bread_total_calc}g.
        """)
elif choice == '3':
    print("""
This function allows you to calculate what bakers percentages your dough comes out to.

In the following prompts please enter your ingredients as they are listet and in weight by grams.

To read more about bakers percentages: https://bakerpedia.com/processes/bakers-percent/
    """)

    bp_flour = float(input("Flour - total by weight in grams: "))
    bp_water = float(input("Water - total by weight in grams: "))
    bp_salt = float(input("Salt - total by weight in grams: "))
    bp_yeast = float(input("Yeast/Levain - total by weight in grams: "))

    bp_total_weight = (bp_flour + bp_water + bp_salt + bp_yeast)
    if bp_total_weight > 0:
        bp = [bp_water, bp_salt, bp_yeast]
        cumulative_percentages = []
        for b in bp:
            percent = (float(b)/float(bp_flour)*100)
            cumulative_percentages.append(percent)
        print(f"""
Flour hydration level is {cumulative_percentages[0]}%
Salt precentage is {cumulative_percentages[1]}%
Yeast/Levain precentage is {cumulative_percentages[2]}%
        """)