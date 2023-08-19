# Puppy - Linemate Backend API

이 프로젝트는 **Linemate**라는 스타트업의 백엔드 API를 작성하는 코드입니다. **Linemate**는 한국을 방문하는 외국인 여행객들이 현지인처럼 한국을 여행할 수 있도록 다양한 현지체험 액티비티와 원데이클래스를 제공하는 여행 스타트업입니다.

## 프로젝트 설명

이 프로젝트는 [FastAPI](https://fastapi.tiangolo.com/)를 기반으로 구축되었으며, RESTful한 API 엔드포인트를 통해 클라이언트와 상호작용합니다. 데이터베이스 연결과 ORM(Object-Relational Mapping)을 활용하여 사용자 정보, 액티비티 정보, 예약 정보 등을 관리하며, 간단한 CRUD(Create, Read, Update, Delete) 기능을 제공합니다.

## 주요 기능

- 사용자 등록, 로그인, 프로필 관리 기능
- 다양한 현지 체험 액티비티 정보 제공
- 액티비티 예약 및 결제 처리
- 관리자용 대시보드와 데이터 관리 기능
- 다국어처리

## 다국어처리
> $ msgfmt locales/ko-KR/LC_MESSAGES/app.po -o locales/ko-KR/LC_MESSAGES/app.mo  
> $ msgfmt locales/en-US/LC_MESSAGES/app.po -o locales/en-US/LC_MESSAGES/app.mo


## 프로젝트 목표

이 프로젝트는 **Linemate** 스타트업의 목표를 달성하기 위해 백엔드 API를 제공합니다. 외국인 여행객들이 한국에서 지역 사람처럼 여행하고 현지 문화와 체험을 즐길 수 있도록 도와주는 핵심 역할을 수행합니다.

**참고:** 이 코드 예시는 간략한 설명을 위한 것으로, 실제 프로젝트에서는 보다 복잡한 로직과 기능이 구현될 것입니다.