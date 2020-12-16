
def arrange_boxes(to_go_in, window, target, history=[], count=0, max=999999999999):
    print(window, target, to_go_in, count)
    if window == target:
        return count
    elif count > max:
        return -1

    if len(window) > 1:
        # swap
        print('try swap')
        s_count = count + 1
        s_window = window[:]
        temp = s_window[0]
        s_window[0] = s_window[1]
        s_window[1] = temp
        if s_window not in history:
            history.append(s_window)
            arrange_boxes(to_go_in, s_window, target, history, s_count, max)

        # rotate
        print('try rotate')
        r_count = count + 1
        r_window = window[:]
        temp = r_window[0]
        # print('x', r_window, r_window[1:])
        r_window = r_window[1:]
        r_window.append(temp)
        if r_window not in history:
            history.append(r_window)
            arrange_boxes(to_go_in, r_window, target, history, r_count, max)

    # add
    if len(to_go_in) != 0:
        print('try adding')
        a_count = count + 1
        a_window = window[:]
        a_to_go_in = to_go_in[:]
        a_window.append(a_to_go_in[0])
        a_to_go_in.remove(a_to_go_in[0])
        if a_window not in history:
            history.append(a_window)
            arrange_boxes(a_to_go_in, a_window, target, history, a_count, max)



print(arrange_boxes(['A', 'B', 'C', 'D'], [], ['A', 'C', 'B', 'D']))
