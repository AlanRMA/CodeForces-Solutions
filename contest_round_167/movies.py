t = int(input())

for _ in range(t):
    # Read number of viewers
    n = int(input())

    # Read opinions for each movie
    movie_a = list(map(int, input().split()))
    movie_b = list(map(int, input().split()))

    # Initialize counters for attitudes
    likes_a = movie_a.count(1)
    dislikes_a = movie_a.count(-1)
    likes_b = movie_b.count(1)
    dislikes_b = movie_b.count(-1)

    # Calculate initial ratings
    rating_a = likes_a - dislikes_a     
    rating_b = likes_b - dislikes_b

    # Initialize review shifts
    neutral_count = 0
    both_liked = 0
    both_disliked = 0
    a_like_b_dislike = 0
    a_dislike_b_like = 0

    # Count occurrences of each case
    for i in range(n):
        if movie_a[i] == 0 and movie_b[i] == 0:
            neutral_count += 1
        elif movie_a[i] == 1 and movie_b[i] == 1:
            both_liked += 1
        elif movie_a[i] == -1 and movie_b[i] == -1:
            both_disliked += 1
        elif movie_a[i] == 1 and movie_b[i] == -1:
            a_like_b_dislike += 1
        elif movie_a[i] == -1 and movie_b[i] == 1:
            a_dislike_b_like += 1

    # Adjust reviews to balance ratings
    # 1. Distribute same-attitude pairs
    rating_a += both_liked
    rating_b += both_liked
    rating_a -= both_disliked
    rating_b -= both_disliked

    # 2. Consider cases with different attitudes
    possible_shifts = min(a_like_b_dislike, a_dislike_b_like)
    rating_a += possible_shifts
    rating_b += possible_shifts

    # 3. Use neutral reviews for remaining balance
    remaining_neutrals = neutral_count + abs(a_like_b_dislike - a_dislike_b_like)
    while remaining_neutrals > 0:
        if rating_a < rating_b:
            rating_a += 1
        else:
            rating_b += 1
        remaining_neutrals -= 1

    # Print the minimum rating
    print(min(rating_a, rating_b))
