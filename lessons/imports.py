"""Examples of imports."""


# Import using an alias
from lessons import helpers as hp

from lessons import helpers

# Import names directly from globals of a module
from lessons.helpers import powerful, THE_ANSWER


def main() -> None:
    # Access the first import
    print(helpers.powerful(2, 4))

    # Access the alias import 
    print(helpers.THE_ANSWER)
    
    # Call the imported funtion directly
    print(powerful(2, 20))
    print(THE_ANSWER)

    print(f"imports.py: {__name__}")

if __name__ == "__main__":
    main()
