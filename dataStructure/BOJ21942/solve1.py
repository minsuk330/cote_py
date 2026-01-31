import sys

def input():
    return sys.stdin.readline().rstrip()

def parse_L_to_minutes(time):
    d_str, hm = time.split('/')
    h_str, m_str = hm.split(':')
    return int(d_str) * 24 * 60 + int(h_str) * 60 + int(m_str)

DAYS_BEFORE_MONTH_2021 = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

def datetime_2021_to_minutes(s: str) -> int:
    date_str, time_str = s.split()
    _, mm, dd = map(int, date_str.split('-'))   # yyyy는 항상 2021이라 버림
    hh, mi = map(int, time_str.split(':'))

    day_of_year_0based = DAYS_BEFORE_MONTH_2021[mm] + (dd - 1)
    return day_of_year_0based * 1440 + hh * 60 + mi

def parse_log_line(line: str):
    # return: (t_minutes, part, member)
    a, b, part, member = line.split()
    t = datetime_2021_to_minutes(f"{a} {b}")
    return t, part, member


#초과 시간에 대한 벌금을 출력 해줘야 한다.
#대여기간 초과시 1분당 penalty를 부과한다.
#(반납-대여)-time 해당 값이 + 일 경우 부과한다.
N,time,penalty = input().split()

rent_paper = {}
fine = {}
for _ in range(int(N)):
    line = input()
    std_time = parse_L_to_minutes(time)
    minutes,part,member = parse_log_line(line)

    key = (member,part)
    if key not in rent_paper:
        rent_paper[(member,part)] = minutes
    else:
        rent_time = rent_paper.pop(key)
        dif = minutes - rent_time

        if dif>std_time:
            fine[member] = fine.get(member,0)+(dif-std_time)*int(penalty)


if not fine:
    print(-1)
else:
    for member in sorted(fine):
        print(f"{member} {fine[member]}")
    