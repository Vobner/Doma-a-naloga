# Input
total_paint = int(input())
paint_needed_per_badge = int(input())
badge_price = int(input())

if (total_paint <= 100 and total_paint <= 100) and (paint_needed_per_badge <= 100 and paint_needed_per_badge <= 100) and (badge_price <= 100 and badge_price <= 100):10

    # Calculate the maximum number of gym badges
    num_badges = total_paint // paint_needed_per_badge

    # Calculate the revenue from selling gym badges
    badge_revenue = num_badges * badge_price

    # Calculate the leftover paint
    leftover_paint = total_paint - (num_badges * paint_needed_per_badge)

    # Calculate the revenue from selling leftover paint
    leftover_revenue = leftover_paint

    # Calculate the total revenue
    total_revenue = badge_revenue + leftover_revenue

    # Output the result
    print(total_revenue)