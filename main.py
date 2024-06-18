from solution import get_total_sequences_and_graduation_probability

if __name__ == "__main__":
    try:
        # test cases
        # N = 5
        no_of_ways_to_attend_classes, graduation_probability = get_total_sequences_and_graduation_probability(5)
        print(graduation_probability)  # output: "14/29"
        # N = 10
        no_of_ways_to_attend_classes, graduation_probability = get_total_sequences_and_graduation_probability(10)
        print(graduation_probability)  # output: "372/773"
    except Exception as e:
        print(f"Exception occurred while running the code : {e}")
      
