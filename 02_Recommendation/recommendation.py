
# ==========================================
# AI WARDROBE ASSISTANT
# RECOMMENDATION MODULE
# ==========================================

clothing_rules = {
    "shirt": [
        "flared trousers",
        "straight-fit trousers",
        "wide-leg jeans"
    ],

    "t-shirt": [
        "baggy jeans",
        "cargo pants",
        "wide-leg trousers"
    ],

    "kurti": [
        "palazzo pants",
        "straight pants",
        "churidar"
    ],

    "short_kurti": [
        "flared jeans",
        "straight-fit jeans",
        "wide-leg trousers"
    ],

    "dress": [
        "sneakers",
        "sandals",
        "heels"
    ],

    "skirt": [
        "fitted top",
        "crop top",
        "blouse"
    ],

    "coat": [
        "wide-leg trousers",
        "straight-fit trousers",
        "jeans"
    ],

    "hoodie": [
        "baggy jeans",
        "cargo pants",
        "wide-leg trousers"
    ],

    "crop_top": [
        "high-waist jeans",
        "wide-leg trousers",
        "flared jeans"
    ],

    "blouse": [
        "wide-leg trousers",
        "flared jeans",
        "long skirt"
    ]
}


color_rules = {

    "red": ["beige", "white", "black", "blue"],
    "blue": ["white", "beige", "black", "grey"],
    "white": ["blue", "beige", "black", "grey"],
    "black": ["blue", "beige", "white", "grey"],
    "beige": ["white", "brown", "black", "blue"],
    "pink": ["white", "beige", "grey", "blue"],
    "green": ["beige", "white", "black", "brown"],
    "brown": ["beige", "cream", "white", "black"],
    "purple": ["white", "black", "beige", "grey"],
    "yellow": ["white", "blue", "beige", "black"]
}


outfit_rules = {

    ("red", "shirt"): [
        "beige flared trousers",
        "white flared trousers",
        "black straight-fit trousers"
    ],

    ("blue", "shirt"): [
        "beige wide-leg trousers",
        "white flared trousers",
        "black wide-leg jeans"
    ],

    ("white", "shirt"): [
        "blue straight-fit jeans",
        "beige flared trousers",
        "black wide-leg trousers"
    ],

    ("black", "shirt"): [
        "blue wide-leg jeans",
        "beige trousers",
        "grey flared trousers"
    ],

    ("green", "shirt"): [
        "beige trousers",
        "white jeans",
        "black wide-leg trousers"
    ],

    ("pink", "shirt"): [
        "white flared trousers",
        "beige trousers",
        "blue jeans"
    ],


    ("red", "t-shirt"): [
        "black cargo pants",
        "blue baggy jeans",
        "beige wide-leg trousers"
    ],

    ("blue", "t-shirt"): [
        "white jeans",
        "beige trousers",
        "black cargo pants"
    ],

    ("white", "t-shirt"): [
        "blue baggy jeans",
        "black cargo pants",
        "beige wide-leg trousers"
    ],

    ("black", "t-shirt"): [
        "blue baggy jeans",
        "grey cargo pants",
        "beige trousers"
    ],


    ("red", "short_kurti"): [
        "cream flared jeans",
        "white flared jeans",
        "dark blue flared jeans"
    ],

    ("pink", "short_kurti"): [
        "white flared jeans",
        "light blue flared jeans",
        "cream flared jeans"
    ],

    ("blue", "short_kurti"): [
        "white flared jeans",
        "cream flared jeans",
        "light blue jeans"
    ],

    ("green", "short_kurti"): [
        "cream flared jeans",
        "white flared jeans",
        "beige trousers"
    ],

    ("black", "short_kurti"): [
        "blue flared jeans",
        "white flared jeans",
        "grey wide-leg jeans"
    ],


    ("red", "kurti"): [
        "cream palazzo pants",
        "beige straight pants",
        "white churidar"
    ],

    ("blue", "kurti"): [
        "white palazzo pants",
        "cream straight pants",
        "beige trousers"
    ],

    ("green", "kurti"): [
        "cream palazzo pants",
        "beige straight pants",
        "white pants"
    ],

    ("pink", "kurti"): [
        "white palazzo pants",
        "cream straight pants",
        "beige pants"
    ],


    ("red", "dress"): [
        "black sandals",
        "white sneakers",
        "beige heels"
    ],

    ("black", "dress"): [
        "white sneakers",
        "black sandals",
        "beige heels"
    ],

    ("blue", "dress"): [
        "white sneakers",
        "beige sandals",
        "white sandals"
    ],

    ("white", "dress"): [
        "white sneakers",
        "brown sandals",
        "black sandals"
    ]
}


footwear_rules = {

    "shirt": [
        "white sneakers",
        "beige sneakers",
        "loafers"
    ],

    "t-shirt": [
        "white sneakers",
        "chunky sneakers"
    ],

    "short_kurti": [
        "white sneakers",
        "juttis",
        "kolhapuris"
    ],

    "kurti": [
        "juttis",
        "kolhapuris",
        "flat sandals"
    ],

    "dress": [
        "white sneakers",
        "sandals",
        "heels"
    ],

    "skirt": [
        "white sneakers",
        "ballet flats"
    ],

    "coat": [
        "boots",
        "white sneakers",
        "loafers"
    ]
}


bag_rules = {

    "red": [
        "beige shoulder bag",
        "black mini bag",
        "cream tote bag"
    ],

    "blue": [
        "white shoulder bag",
        "beige tote bag",
        "black mini bag"
    ],

    "white": [
        "black shoulder bag",
        "brown mini bag",
        "beige tote bag"
    ],

    "black": [
        "black mini bag",
        "beige shoulder bag",
        "white tote bag"
    ],

    "beige": [
        "brown shoulder bag",
        "cream tote bag",
        "black mini bag"
    ],

    "pink": [
        "white shoulder bag",
        "beige mini bag",
        "brown mini bag"
    ],

    "green": [
        "brown shoulder bag",
        "beige tote bag",
        "black mini bag"
    ],

    "brown": [
        "cream tote bag",
        "beige shoulder bag",
        "black mini bag"
    ]
}


accessory_rules = {

    "shirt": {
        "western": [
            "minimal gold jewellery",
            "small hoops",
            "delicate watch"
        ]
    },

    "t-shirt": {
        "western": [
            "small hoops",
            "layered necklace",
            "minimal bracelet"
        ]
    },

    "short_kurti": {
        "traditional": [
            "oxidised jhumkas",
            "oxidised bangles",
            "small oxidised necklace"
        ]
    },

    "kurti": {
        "traditional": [
            "oxidised jhumkas",
            "oxidised bangles",
            "statement earrings"
        ]
    },

    "dress": {
        "western": [
            "minimal gold jewellery",
            "delicate necklace",
            "small hoops"
        ]
    }
}


hairstyle_rules = {

    "shirt": [
        "soft waves",
        "low messy bun",
        "half-up half-down"
    ],

    "t-shirt": [
        "high ponytail",
        "messy bun",
        "beach waves"
    ],

    "short_kurti": [
        "soft waves",
        "half-up half-down",
        "messy low bun"
    ],

    "kurti": [
        "low bun",
        "soft waves",
        "messy low bun"
    ],

    "dress": [
        "beach waves",
        "low bun",
        "soft waves"
    ],

    "skirt": [
        "high ponytail",
        "half-up half-down",
        "soft waves"
    ],

    "coat": [
        "sleek straight hair",
        "high ponytail",
        "low bun"
    ]
}


color_hairstyle_rules = {

    ("red", "shirt"): [
        "soft waves",
        "low messy bun"
    ],

    ("blue", "shirt"): [
        "half-up half-down",
        "soft waves"
    ],

    ("black", "shirt"): [
        "sleek straight hair",
        "low bun"
    ],

    ("white", "shirt"): [
        "soft waves",
        "half-up half-down"
    ],

    ("pink", "short_kurti"): [
        "soft waves",
        "half-up half-down"
    ],

    ("red", "short_kurti"): [
        "messy low bun",
        "soft waves"
    ],

    ("green", "short_kurti"): [
        "low bun",
        "soft waves"
    ],

    ("blue", "short_kurti"): [
        "half-up half-down",
        "soft waves"
    ],

    ("black", "dress"): [
        "sleek straight hair",
        "low bun"
    ],

    ("red", "dress"): [
        "beach waves",
        "low bun"
    ]
}


final_look_rules = {

    ("red", "shirt"): {
        "bottom": "beige flared trousers",
        "shoes": "white sneakers",
        "bag": "beige shoulder bag",
        "accessories": "minimal gold jewellery + small hoops",
        "hairstyle": "soft waves",
        "vibe": "Clean + Chic"
    },

    ("blue", "shirt"): {
        "bottom": "beige wide-leg trousers",
        "shoes": "white sneakers",
        "bag": "white shoulder bag",
        "accessories": "minimal silver jewellery",
        "hairstyle": "half-up half-down",
        "vibe": "Clean + Effortless"
    },

    ("white", "shirt"): {
        "bottom": "blue straight-fit jeans",
        "shoes": "white sneakers",
        "bag": "black mini bag",
        "accessories": "minimal gold jewellery",
        "hairstyle": "soft waves",
        "vibe": "Classic + Pinterest-coded"
    },

    ("black", "shirt"): {
        "bottom": "blue wide-leg jeans",
        "shoes": "white sneakers",
        "bag": "black mini bag",
        "accessories": "silver jewellery",
        "hairstyle": "sleek straight hair",
        "vibe": "Cool + Edgy"
    },

    ("red", "short_kurti"): {
        "bottom": "cream flared jeans",
        "shoes": "juttis",
        "bag": "beige sling bag",
        "accessories": "oxidised jhumkas + oxidised bangles",
        "hairstyle": "messy low bun",
        "vibe": "Indo-Western + Chic"
    },

    ("pink", "short_kurti"): {
        "bottom": "white flared jeans",
        "shoes": "white sneakers",
        "bag": "beige shoulder bag",
        "accessories": "oxidised jhumkas + delicate bracelet",
        "hairstyle": "soft waves",
        "vibe": "Soft Girl + Indo-Western"
    },

    ("blue", "short_kurti"): {
        "bottom": "white flared jeans",
        "shoes": "white sneakers",
        "bag": "white shoulder bag",
        "accessories": "oxidised earrings",
        "hairstyle": "half-up half-down",
        "vibe": "Fresh + Effortless"
    },

    ("green", "short_kurti"): {
        "bottom": "cream flared jeans",
        "shoes": "juttis",
        "bag": "brown shoulder bag",
        "accessories": "oxidised jhumkas",
        "hairstyle": "low messy bun",
        "vibe": "Earthy + Desi Chic"
    },

    ("red", "kurti"): {
        "bottom": "cream palazzo pants",
        "shoes": "juttis",
        "bag": "beige potli bag",
        "accessories": "oxidised jhumkas + bangles",
        "hairstyle": "low bun",
        "vibe": "Elegant + Desi"
    },

    ("pink", "kurti"): {
        "bottom": "white palazzo pants",
        "shoes": "juttis",
        "bag": "cream shoulder bag",
        "accessories": "oxidised jhumkas",
        "hairstyle": "soft waves",
        "vibe": "Soft + Feminine"
    },

    ("black", "dress"): {
        "bottom": "—",
        "shoes": "white sneakers",
        "bag": "black mini bag",
        "accessories": "minimal silver jewellery",
        "hairstyle": "sleek straight hair",
        "vibe": "Minimal + Expensive-looking"
    },

    ("red", "dress"): {
        "bottom": "—",
        "shoes": "black sandals",
        "bag": "black mini bag",
        "accessories": "minimal gold jewellery",
        "hairstyle": "beach waves",
        "vibe": "Bold + Elegant"
    }
}


def recommend_outfit(item, color=None):

    item = item.lower()

    if color:
        color = color.lower()

    if color and (color, item) in outfit_rules:
        outfit_options = outfit_rules[(color, item)]
    else:
        outfit_options = clothing_rules.get(item, [])

    shoes = footwear_rules.get(item, [])

    bags = bag_rules.get(color, []) if color else []

    if color and (color, item) in color_hairstyle_rules:
        hairstyles = color_hairstyle_rules[(color, item)]
    else:
        hairstyles = hairstyle_rules.get(item, [])

    if item in accessory_rules:

        if item in ["kurti", "short_kurti"]:
            accessories = accessory_rules[item]["traditional"]
        else:
            accessories = accessory_rules[item]["western"]

    else:
        accessories = []

    final_look = final_look_rules.get((color, item), None)

    return {
        "outfit_options": outfit_options,
        "shoes": shoes,
        "bags": bags,
        "hairstyles": hairstyles,
        "accessories": accessories,
        "final_look": final_look
    }


def create_final_look(color, item):

    final = final_look_rules.get((color, item))

    if final:
        return final

    outfit_options = outfit_rules.get((color, item), [])
    shoes = footwear_rules.get(item, [])
    bags = bag_rules.get(color, [])

    hairstyles = color_hairstyle_rules.get(
        (color, item),
        hairstyle_rules.get(item, [])
    )

    return {
        "bottom": outfit_options[0] if outfit_options else "choose a compatible bottom",
        "shoes": shoes[0] if shoes else "neutral sneakers",
        "bag": bags[0] if bags else "neutral shoulder bag",
        "accessories": "minimal accessories",
        "hairstyle": hairstyles[0] if hairstyles else "soft waves",
        "vibe": "Effortless + Chic"
    }


def explain_final_look(color, item, final):

    explanation = []

    explanation.append(
        f"The {color} {item} pairs well with "
        f"{final['bottom']} for a balanced colour combination."
    )

    explanation.append(
        f"{final['shoes'].capitalize()} keeps the outfit "
        f"comfortable and coordinated."
    )

    explanation.append(
        f"{final['bag'].capitalize()} complements the overall colour palette."
    )

    explanation.append(
        f"{final['accessories'].capitalize()} complete the look "
        f"without making it look too heavy."
    )

    explanation.append(
        f"{final['hairstyle'].capitalize()} matches the overall outfit vibe."
    )

    explanation.append(
        f"Overall vibe: {final['vibe']} ✨"
    )

    return explanation


def get_complete_recommendation(item, color):

    item = item.lower()
    color = color.lower()

    result = recommend_outfit(item, color)

    final = create_final_look(color, item)

    return {
        "clothing": f"{color.title()} {item.replace('_', ' ').title()}",
        "outfit_options": result["outfit_options"],
        "shoes": result["shoes"],
        "bags": result["bags"],
        "accessories": result["accessories"],
        "hairstyles": result["hairstyles"],
        "final_look": final,
        "explanation": explain_final_look(color, item, final)
    }
