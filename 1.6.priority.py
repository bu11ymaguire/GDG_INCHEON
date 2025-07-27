import json

# 이전에 생성한 JSON 데이터를 로드합니다.
# 실제 환경에서는 파일을 읽어오겠지만, 여기서는 변수로 직접 선언합니다.
JSON_DATA = """
{
  "컨퍼런스명": "Google I/O Extended Incheon 2025",
  "날짜": "2025년 7월 26일 (토)",
  "트랙별 액티비티": {
    "Keynote": [
      { "시간": "13:00-13:10", "제목": "Keynote", "연사": "Incheon Organizer", "난이도": "전체", "목적": "컨퍼런스 소개 및 개요", "설명": "..." }
    ],
    "AI": [
      { "시간": "13:10-13:50", "제목": "1인 개발자를 위한 LLM 서비스 빠르게 만들어보기", "연사": "차승온 (Google Developer Expert)", "난이도": "중급", "목적": "실용적 기술 습득", "설명": "..." },
      { "시간": "14:00-14:40", "제목": "운영 비-머신러닝 엔지니어의 LLM 서비스 도입기: 뭘 알아야 할까요?", "연사": "방문주 | 마이리얼트립", "난이도": "초급", "목적": "기술 도입 전략", "설명": "..." },
      { "시간": "14:50-15:30", "제목": "LLM을 위한 데이터 파이프라인 구축 with MaxText on TPUs", "연사": "박정세", "난이도": "고급", "목적": "심층 기술 탐구", "설명": "..." },
      { "시간": "15:40-16:20", "제목": "미디어 파이프라인 구축 2025년 AI 기술 도입기", "연사": "이상협 | 클래스101", "난이도": "중급", "목적": "최신 기술 동향 및 사례 연구", "설명": "..." },
      { "시간": "16:30-17:10", "제목": "생성형 AI를 활용하여 어드벤처 게임 제작기", "연사": "안혜연", "난이도": "중급", "목적": "창의적 프로젝트 개발", "설명": "..." },
      { "시간": "17:20-18:00", "제목": "Gemma for Your Device", "연사": "황준", "난이도": "중급", "목적": "최신 기술 동향 및 사례 연구", "설명": "..." }
    ],
    "General": [
      { "시간": "13:10-13:50", "제목": "Google I/O 2025 Extended Incheon 다시보기", "연사": "배준석 | GDG Korea Android Organizer", "난이도": "전체", "목적": "기술 트렌드 파악", "설명": "..." },
      { "시간": "14:00-14:40", "제목": "기억, 기록, 그리고 아카이브: 구글 포토, 구글 드라이브, 구글 원 A-Z", "연사": "이해봄 | Google Product Expert", "난이도": "초급", "목적": "생산성 향상", "설명": "..." },
      { "시간": "14:50-15:30", "제목": "#N년차 개발 블로그, 그를 하며 얻은 것들", "연사": "정상춘", "난이도": "전체", "목적": "경험 공유 및 커리어 개발", "설명": "..." },
      { "시간": "15:40-16:20", "제목": "개발자 개인 공부가 아닌 협업을 하자", "연사": "김종민 | 우아한형제들", "난이도": "전체", "목적": "개발 문화 및 협업", "설명": "..." },
      { "시간": "16:30-17:10", "제목": "바이브럴 시대에 살아가는 개발자가 되는 방법", "연사": "이정우 | Konkuk Univ.", "난이도": "전체", "목적": "커리어 개발 및 트렌드", "설명": "..." },
      { "시간": "17:20-18:00", "제목": "평범한 환경의 내가 성장하는 법", "연사": "최선필 | Konkuk Univ. | NAVER", "난이도": "전체", "목적": "커리어 개발 및 동기부여", "설명": "..." }
    ],
    "Mobile": [
      { "시간": "13:10-13:50", "제목": "Firebase Dynamic Links의 중단, 그리고 Fireship으로의 마이그레이션 여정", "연사": "정희종 | GDG Incheon Organizer", "난이도": "중급", "목적": "문제 해결 및 마이그레이션", "설명": "..." },
      { "시간": "14:00-14:40", "제목": "Flutter 프로젝트에 Unity 콘텐츠를 임베드하여 나만의 특별한 앱 만들기", "연사": "윤예지", "난이도": "고급", "목적": "심층 기술 탐구", "설명": "..." },
      { "시간": "14:50-15:30", "제목": "What's New in Android", "연사": "허성실 | GDG Incheon Organizer", "난이도": "초급", "목적": "최신 기술 업데이트", "설명": "..." },
      { "시간": "15:40-16:20", "제목": "What's New in Compose & Declarative UI Development Tools", "연사": "조민성 | Moloco", "난이도": "중급", "목적": "최신 기술 업데이트", "설명": "..." },
      { "시간": "16:30-17:10", "제목": "What's New in Adaptive Android Development", "연사": "오승현 | Google", "난이도": "중급", "목적": "최신 기술 업데이트", "설명": "..." },
      { "시간": "17:20-18:00", "제목": "안드로이드 아키텍트가 되어보자", "연사": "김상현 | 스캐터랩", "난이도": "중급", "목적": "기초 다지기 및 아키텍처 설계", "설명": "..." }
    ],
    "Tech": [
      { "시간": "13:10-13:50", "제목": "안드로이드에서 고성능을 달성하는 방법", "연사": "양찬석 | Toss", "난이도": "고급", "목적": "성능 최적화", "설명": "..." },
      { "시간": "14:00-14:40", "제목": "웹사이트 서버를 어떻게 반응형으로 만들까?", "연사": "이동규", "난이도": "중급", "목적": "백엔드 개발", "설명": "..." },
      { "시간": "14:50-15:30", "제목": "Understanding Kotlin Multiplatform", "연사": "이성민 | Republic", "난이도": "중급", "목적": "크로스플랫폼 개발", "설명": "..." },
      { "시간": "15:40-16:20", "제목": "개인 서버리스 아키텍처 A to Z", "연사": "신정's", "난이도": "중급", "목적": "클라우드 및 인프라", "설명": "..." },
      { "시간": "16:30-17:10", "제목": "작은 스타트업의 디자인 시스템, 어떻게 만들어야 할까?", "연사": "윤소정", "난이도": "초급", "목적": "디자인 시스템 및 협업", "설명": "..." },
      { "시간": "17:20-18:00", "제목": "검색 플랫폼 구축기", "연사": "장동수", "난이도": "고급", "목적": "심층 기술 탐구", "설명": "..." }
    ],
    "Hands-on": [
      { "시간": "13:10-14:40", "제목": "Firebase Studio로 답례품 애플리케이션 만들기", "연사": "박강성", "난이도": "초급", "목적": "실습 및 코드랩", "설명": "..." },
      { "시간": "14:50-16:20", "제목": "Gemini API의 새로운 기능을 모두 이용하여 나만의 길로 바로 길 안내받기!", "연사": "최완복", "난이도": "중급", "목적": "실습 및 코드랩", "설명": "..." },
      { "시간": "16:30-18:00", "제목": "How to build beautiful apps with Flutter", "연사": "박세리 | Women Techmakers", "난이도": "초중급", "목적": "실습 및 코드랩", "설명": "..." }
    ]
  }
}
"""

data = json.loads(JSON_DATA)

# 모든 세션을 하나의 리스트로 통합
all_sessions = []
for track, sessions in data['트랙별 액티비티'].items():
    if track == 'Keynote': continue # 키노트는 제외
    for session in sessions:
        session['트랙'] = track
        all_sessions.append(session)

def get_time_slots(time_str):
    """'HH:MM-HH:MM' 형식의 문자열을 분 단위 슬롯 리스트로 변환"""
    start_str, end_str = time_str.split('-')
    start_h, start_m = map(int, start_str.split(':'))
    end_h, end_m = map(int, end_str.split(':'))
    
    start_total_minutes = start_h * 60 + start_m
    end_total_minutes = end_h * 60 + end_m
    
    # 10분 단위로 슬롯 생성
    return list(range(start_total_minutes, end_total_minutes, 10))


def calculate_score(session, profile):
    """세션과 프로필을 기반으로 점수 계산"""
    score = 0
    # 1. 트랙 점수
    if session['트랙'] in profile['preferred_tracks']:
        score += 5
    # 2. 난이도 점수
    if session['난이도'] in profile['preferred_difficulties']:
        score += 3
    if session['난이도'] == '전체': # '전체' 난이도는 누구나 듣기 좋으므로 기본 점수 부여
        score += 1
    # 3. 목적 점수
    if session['목적'] in profile['preferred_purposes']:
        score += 4
    return score

def recommend_schedule(profile, sessions):
    """프로필에 맞는 최적의 시간표 추천"""
    
    # 시간 순서대로 세션 정렬
    sorted_sessions = sorted(sessions, key=lambda x: x['시간'].split('-')[0])
    
    recommended = []
    scheduled_slots = set()
    
    # 각 세션을 순회하며 최적의 선택을 찾음
    for session in sorted_sessions:
        session_slots = get_time_slots(session['시간'])
        
        # 이미 예약된 시간과 겹치는지 확인
        if not set(session_slots).isdisjoint(scheduled_slots):
            continue

        # 현재 시작 시간에 들을 수 있는 다른 세션들을 찾음
        start_time = session['시간'].split('-')[0]
        competing_sessions = [s for s in sorted_sessions if s['시간'].split('-')[0] == start_time and not set(get_time_slots(s['시간'])).isdisjoint(scheduled_slots)]
        
        if not competing_sessions:
            continue

        # 경쟁 세션들 중 가장 점수가 높은 세션을 선택
        best_session_for_slot = max(competing_sessions, key=lambda s: calculate_score(s, profile))
        
        # 이전에 추가되지 않았다면 추가
        if best_session_for_slot not in recommended:
            recommended.append(best_session_for_slot)
            # 선택된 세션의 시간 슬롯을 예약 처리
            scheduled_slots.update(get_time_slots(best_session_for_slot['시간']))
            
    # 최종 추천 목록을 시간 순으로 다시 정렬
    return sorted(recommended, key=lambda x: x['시간'].split('-')[0])


# --- 추천 알고리즘 실행 ---

# 1. 사용자 프로필 정의
profile_ai_expert = {
    "name": "AI 기술 전문가 🧑‍💻",
    "preferred_tracks": ["AI", "Tech"],
    "preferred_difficulties": ["중급", "고급"],
    "preferred_purposes": ["심층 기술 탐구", "실용적 기술 습득", "성능 최적화"]
}

profile_mobile_beginner = {
    "name": "모바일 앱 개발 입문자 📱",
    "preferred_tracks": ["Mobile", "Hands-on", "General"],
    "preferred_difficulties": ["초급", "초중급", "전체"],
    "preferred_purposes": ["실습 및 코드랩", "최신 기술 업데이트", "기초 다지기 및 아키텍처 설계"]
}

# 2. 프로필에 따른 추천 실행
recommendation1 = recommend_schedule(profile_ai_expert, all_sessions)
recommendation2 = recommend_schedule(profile_mobile_beginner, all_sessions)


# 3. 결과 출력
def print_recommendation(profile, schedule):
    print("="*50)
    print(f"✅ 추천 스케줄: {profile['name']}")
    print("="*50)
    for session in schedule:
        print(f"[{session['시간']}] {session['제목']} ({session['트랙']} | {session['난이도']})")
    print("\n")

print_recommendation(profile_ai_expert, recommendation1)
print_recommendation(profile_mobile_beginner, recommendation2)