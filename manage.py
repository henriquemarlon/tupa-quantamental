from pre_processed_data.processment import price_fixing
from data_treatment.bob import main

if __name__ == "__main__":
    try:
        price_fixing()

    except:
        main()
        price_fixing()
