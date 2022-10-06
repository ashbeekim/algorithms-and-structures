# Algorithms & Structures

코드를 짤 때에 고려해야 할 것들 중 일부만 나열하면, 순서, 구조, 논거 등이 있다.

영어로는 Algorithm, Structure, Logic 으로 불리는 단어가 프로그래밍에서 왜 중요할까?
* [Algorithm](https://en.wikipedia.org/wiki/Algorithm) [^wiki_algorithm]
      주로 I/O, DP, Sort, Stack, Queue, Deque, Binary Search, Ternary Search, Graph, Greedy, Brute Force, Divide and Conquer 등을 공부하라고 하던데, 빠르고 적은 용량 처리를 위한 계산 순서라고만 정의를 하기엔 개인적인 이해가 부족한 듯 하다.
* Structure [^wiki_structure_list]
      구조는 차원 혹은 계층을 어디까지 확장하는가를 제외하면 home을 기준으로, 깃헙의 오픈 소스를 참고하면 다음과 같이 구성된 경우를 종종 확인할 수 있다.
    ```
    $ tree
    .
    ├── (bin)
    ├── config(or conf)
    ├── (lib)
    ├── ...
    ├── module(or model)
    ├── (script)
    ├── src
    │   ├── (contents)
    │   ├── (fonts)
    │   ├── ...
    │   └── images
    └── test
    ```
    라이센스에 따라서, 때로는 주 사용되는 서비스 혹은 언어에 따라서 상세한 구조는 달라지지만, 구조를 파악해야 전반적인 흐름을 알 수 있다. 복수로 명시하는 경우나 동사로 표기하는 경우에 대해서도 알아보면 구조 파악에 도움이 된다.(물론 나와 같은 신입 수준에서는 할당된 업무 그 외의 것을 할 수도 할 필요도 없다.)

* [Logic](https://en.wikipedia.org/wiki/Logic) [^wiki_logic]
    ```
    Logic is traditionally defined as the study of the laws of thought or correct reasoning.
    ```
    사전적 정의 중 해당 인용구를 발췌한 이유는 laws를 일반적으로 알고 있는 '법'의 의미를 '규칙', '사규', '정책' 등 입체적으로 바꾸면 프로그래밍에서 'logic'의 중요성을 알 수 있기 때문이다.


## Contexts
* [BAEKJOON](#baekjoon)
* [Programmers](#programmers)
* [LeetCode](#leetcode)
* [HackerRank](#hackerrank)

제일 많은 시간을 내어 공부하고 있는 플랫폼은 [Sololearn](https://www.sololearn.com/profile/21362772), [Google Cloud Qwiklabs](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24)(혹은 Kaggle) 정도라서 내용이 뒤죽박죽이 될까봐 걱정되지만, 내용 중 알고리즘이나 자료구조, 그리고 쿼리문 증 공유가 되면 재밌겠는 생각이 들면 여기나 cs-archive에 commit 하겠다.


---
### [BAEKJOON](https://www.acmicpc.net/step)
  백준은 단계별로 풀이를 하면, 50단계까지 있어서 이전에 작성했던 코드나 가끔 아무 생각없이 코드만 치고 싶을 때 조금씩 업데이트 할 예정이다.

| step | title | languages | remarks|
|:----:|-------|-----------|--------|
| 1 | [입출력과 사칙연산](https://www.acmicpc.net/step/1) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_1.py)</li></ul> | - |
| 2 | [조건문](https://www.acmicpc.net/step/4) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_2.py)</li></ul> | - |
| 3 | [반복문](https://www.acmicpc.net/step/3) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_3.py)</li></ul> | - |
| 4 | [1차원 배열](https://www.acmicpc.net/step/6) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_4.py)</li></ul> | - |
| 5 | [함수](https://www.acmicpc.net/step/5) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_5.py)</li></ul> | - |
| 6 | [문자열](https://www.acmicpc.net/step/7) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_6.py)</li></ul> | - |
| 7 | [기본 수학 1](https://www.acmicpc.net/step/8) | <ul><li style="list-style-type:none;"> - [x] [Python3](./baekjoon/python3/step_7.py)</li></ul> | - |
| 8 | [기본 수학 2](https://www.acmicpc.net/step/10) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_8.py)</li></ul> | - |
| 9 | [정렬](https://www.acmicpc.net/step/9) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_9.py)</li></ul> | - |
| 10 | [재귀](https://www.acmicpc.net/step/19) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_10.py)</li></ul> | - |
| 11 | [브루트 포스](https://www.acmicpc.net/step/22) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_11.py)</li></ul> | - |
| 12 | [집합과 맵](https://www.acmicpc.net/step/49) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_12.py)</li></ul> | - |
| 13 | [기하 1](https://www.acmicpc.net/step/50) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_13.py)</li></ul> | - |
| 14 | [정수론 및 조합론](https://www.acmicpc.net/step/18) | <ul><li style="list-style-type:none;"> - [ ] [Python3](./baekjoon/python3/step_14.py)</li></ul> | - |
| ... | ... | ... | ... |
| 53 | [매우 어려운 자료구조와 알고리즘(수정 예정)](https://www.acmicpc.net/step/46) | - | - |


---
### [Programmers](https://programmers.co.kr/learn/challenges)
  프로그래머스에서의 쿼리 데이터는 ODbL을 따르며 Kaggle에서의 데이터를 활용했다. 고난도의 쿼리가 많으면, 재밌게 DB 공부를 할 수 있을 것 같은데 대체적으로 R(read)에 치중된 내용이라 사이트 내 더 데이터가 쌓일 때까지는 Google BigQuery로 C(create), U(update)를 실습하면 좋을 듯 하다.(Delete는 아직 무서워서...)

  Oracle, MySQL 중 선택이 가능한데, 압도적으로 뛰어난 게 아니면 하나에만 집중하란 말을 많이 듣기도 공감도 하기에 MySQL로 풀었다. 그러나 복습이 필요하다 생각들 때 Oracle로 플면 좋을 것 같아서, 우선은 보류.

  알고리즘은 가볍게 시작하기엔 프로그래머스가 좋다고 생각한다. 모든 문제로 가면, 더 많은 문재를 볼 수 있지만 급할 땐 고득점 Kit로 연습하면 되기 때문이다. 다양한 언어가 있지만, '한 놈만 팬다.'는 여기서도 적용되기에 일단 Python으로 진행하겠다.
> #### Query

| level | section | division | languages |
|:-------|:---------|:---------:|:----------|
| 1 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) | [SELECT](https://programmers.co.kr/learn/courses/30/parts/17042) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| 1 to 2 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) |[SUM, MAX, MIN](https://programmers.co.kr/learn/courses/30/parts/17043) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| 2 and 4 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) | [GROUP BY](https://programmers.co.kr/learn/courses/30/parts/17044) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| 1 to 2 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) | [IS NULL](https://programmers.co.kr/learn/courses/30/parts/17045) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| 3 to 4 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) | [JOIN](https://programmers.co.kr/learn/courses/30/parts/17046) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| 2 to 3 | [SQL High Score Kit](https://programmers.co.kr/learn/challenges?tab=sql_practice_kit) | [String, Date](https://programmers.co.kr/learn/courses/30/parts/17047) | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |
| under 5 | [모든 문제](https://programmers.co.kr/learn/challenges?tab=all_challenges) | - | <ul><li style="list-style-type:none;"> - [x] MySQL</li><li style="list-style-type:none;"> - [ ] Oracle</li></ul> |

<!--| <ul><li style="list-style-type:none;">&#9745; MySQL</li><li style="list-style-type:none;">&#9744;  Oracle</li></ul> | -->

> #### Algorithms

| level | section | division | languages |
|:-------|:---------|:---------:|:----------|
| 1 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Hash](https://programmers.co.kr/learn/courses/30/parts/12077) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Stack/Queue](https://programmers.co.kr/learn/courses/30/parts/12081) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 2 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Heap](https://programmers.co.kr/learn/courses/30/parts/12117) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Sort](https://programmers.co.kr/learn/courses/30/parts/12198) |  <ul><li style="list-style-type:none;"> - [x] [Python3](./programmers/python3/sort.py)</li></ul> |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Brute Force](https://programmers.co.kr/learn/courses/30/parts/12230) | <ul><li style="list-style-type:none;"> - [x] [Python3](./programmers/python3/brute-force.py)</li></ul> |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Greedy](https://programmers.co.kr/learn/courses/30/parts/12244) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 3 to 4 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Dynamic Programming](https://programmers.co.kr/learn/courses/30/parts/12263) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 2 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [DFS/BFS](https://programmers.co.kr/learn/courses/30/parts/12421) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 3 to 4 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Binary Search](https://programmers.co.kr/learn/courses/30/parts/12486) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| 3 and 5 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Graph](https://programmers.co.kr/learn/courses/30/parts/14393) | <ul><li style="list-style-type:none;"> - [ ] Python3</li></ul> |
| no more than 5 | [모든 문제](https://programmers.co.kr/learn/challenges?tab=all_challenges) | - | - |


---
### [LeetCode](https://leetcode.com/problemset/all/)
풀이할 문제 이름부터 직관적이기도 하고, 알고리즘, DB, 스크립트 등 다양하게 연습을 할 수 있는 곳이기도 하다. 기본으로 제공된 문제를 다 풀이한 사람은 프리미엄 구독도 기꺼이 할 것 같은 생각이 들게하는 알고리즘 문제 풀이 플랫폼인 리트코드. 글로벌한 대기업의 인터뷰 자료나 코딩테스트 준비에도 좋은 플랫폼이라고 생각은 들지만, 유일한 단점은 영어를 읽을 줄 알아야 한다.

[책만 | 파이썬 알고리즘 인터뷰(박상길 지음, 정진호 일러스트)](https://github.com/onlybooks/algorithm-interview)는 해당 도서의 깃헙 레포지토리로, 리트코드를 중심으로 코딩 테스트 방법을 설명한 책인데, 참고해서 연습을 하다보면 보다 많은 방법을 시도해 볼 수 있다. 우아한 풀이라고 불리는 풀이법이 여럿 보이지만, 막 공부를 시작한 내 수준에서 이해하기 어려운 내용이 많기 때문에 가끔은 알고 있는 수준에서 문제를 풀이하고자 [extra_easy](./leetcode/extra_easy.py)로 시간 날 때 풀이할 계획이나, 당분간 책을 바탕으로 구조나 알고리즘에 대한 이해를 높이는 것을 우선으로 하고 있다.


---
### [HackerRank](https://www.hackerrank.com/)
가입을 하면 1 Month Preparation Kit이란 이름으로 4주 정도의 풀이할 알고리즘 리스트가 제공된다. 각 주차의 문제를 풀이하고 나면, Mock Test까지 제공되는데 이런 저런 이유로 활동이 겹치다보니 주차의 문제를 풀어나가기에 급급해서 아직 시도하진 않았다.

가급적 해당 플랫폼의 문제는 혼자 힘으로 풀이하고 싶다는 이유로 막히면 일단 다른 플랫폼에서 머리를 식히거나, 다른 일이나 공부를 하다가 다시 들어오면 풀리는 신기한(?) 체험을 할 수 있다. LeetCode에서 언급한 책의 내용과 같은 우아한 풀이는 없지만, 그냥 궁금한 분들은 다음 링크를 참고하길.

* [week1](./hackerrank/week1.py)
* [week2](./hackerrank/week2.py)


---
[^wiki_algorithm]: 계산의 순서로만 이해하기엔, 충분한 설명이 아닌 것 같아서 조금 더 참고한 뒤 수정하겠음.
[^wiki_structure_list]: 직군에 따라 우선적으로 파악해야 할 구조가 다를 것이기에 다음의 위키피디아 링크로 대체하나, 혹시 한국 지원이 되지 않는 링크라면 목차나 키워드만 파악 후 `Pattern`, `Flow`, 혹은 `Architecture` 등의 `Structure`와 유사한 의미를 가진 단어와 사용 언어, 목차/키워드를 조합해 검색하면 이미지 파일로 확인이 가능하다.(그 후 github 내 관심 라이브러리 소스의 `tree`를 확인하는 것도 큰 틀을 파악하기 좋은 방법이다.)
    * [Software Architecture](https://en.wikipedia.org/wiki/Software_architecture)
    * [Data Structure](https://en.wikipedia.org/wiki/Data_structure)
    * [Structure_(mathematical_logic)](https://en.wikipedia.org/wiki/Structure_(mathematical_logic))
[^wiki_logic]: 로직에 대한 내용 중 `Systems of logic`이나 `Areas of research`의 내용을 참고해서 다양한 차원에서 프로그래밍적인 고려 사항을 연결할 수 있다면 좋겠다만, 현재 나의 수준에선 Paper's Abstact 내 필수 키워드 참고 용도로만 사용 중이다.