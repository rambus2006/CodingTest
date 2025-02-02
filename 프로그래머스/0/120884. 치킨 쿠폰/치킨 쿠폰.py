def solution(chicken):
    total_service = 0  # 서비스 치킨 개수
    coupon = chicken  # 처음에는 주문한 치킨 수만큼 쿠폰이 있음

    while coupon >= 10:
        service = coupon // 10  # 서비스 치킨 개수
        total_service += service
        coupon = coupon % 10 + service  # 남은 쿠폰 + 새로 얻은 쿠폰
    
    return total_service