def users_visited_both_pages(pageA, pageB):
    return pageA.intersection(pageB)

def users_visited_either_but_not_both(pageA, pageC):
    all_visiters=pageA.union(pageC)
    common=pageA.intersection(pageC)
    return all_visiters.difference(common)

def update_page_a(pageA, new_user_ids):
    pageA.update(new_user_ids)
    return pageA

def remove_from_page_b(pageB, users_to_remove):
    pageB.difference_update(users_to_remove)
    return pageB

page_a_visitors = {'user1', 'user2', 'user3', 'user4'}
page_b_visitors = {'user2', 'user3', 'user5'}
page_c_visitors = {'user1', 'user5', 'user6'}

both_pages_visitors = users_visited_both_pages(page_a_visitors, page_b_visitors)
print("Users who visited both Page A and Page B:", both_pages_visitors)

either_but_not_both = users_visited_either_but_not_both(page_a_visitors, page_c_visitors)
print("Users who visited either Page A or Page C, but not both:", either_but_not_both)

new_users = {'user7', 'user8'}
updated_page_a = update_page_a(page_a_visitors, new_users)
print("Updated Page A visitors:", updated_page_a)

users_to_remove = {'user2'}
updated_page_b = remove_from_page_b(page_b_visitors, users_to_remove)
print("Updated Page B visitors:", updated_page_b)
