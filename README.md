# git-actions-practice

Git + GitHub Actions 실무 연습 프로젝트.

## 브랜치 전략

trunk-based development 기반.

| 브랜치 | 용도 |
|---|---|
| `main` | 배포 브랜치. 직접 push 금지, PR 필수 |
| `feat/*` | 기능 개발 |
| `fix/*` | 버그 수정 |
| `chore/*` | 설정, 의존성 등 |

## 로컬 실행

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## 테스트

```bash
pytest
```
