from chronological import read_prompt, fetch_max_search_doc, main, cleaned_completion

async def fetch_three_top_animals(query, n):
    # splitting on ',' -- similar to what you might do with a csv file
    prompt_animals = read_prompt('animals').split(',')
    return await fetch_max_search_doc(query, prompt_animals, engine="ada", n=n)


async def basic_example_with_variables():
    pass

def map_favorite_animals_to_foods():
    pass

async def logic():
    pass

main(logic)