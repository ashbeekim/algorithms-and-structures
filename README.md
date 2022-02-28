# Algorithms & Structures

처음 학원을 다닐 때와 지금을 비교하면, 코드를 짜는 방식이나 고려하는 지점이 달라졌다.
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
    라이센스에 따라서, 때로는 주 사용되는 서비스 혹은 언어에 따라서 상세한 구조는 달라지지만, 구조를 파악해야 전반적인 흐름을 알 수 있다. 복수로 명시하는 경우나 동사로 표기하는 경우에 대해서도 알아보면 구조 파악에 도움이 된다.

* [Logic](https://en.wikipedia.org/wiki/Logic) [^wiki_logic]
    ```
    Logic is traditionally defined as the study of the laws of thought or correct reasoning.
    ```
    사전적 정의 중 해당 인용구를 발췌한 이유는 laws를 일반적으로 알고 있는 '법'의 의미를 '규칙', '사규', '정책' 등 입체적으로 바꾸면 프로그래밍에서 'logic'의 중요성을 알 수 있기 때문이다.


## Contexts
* [BAEKJOON](baekjoon)
* [Programmers](programmers)

---
### [BAEKJOON](https://www.acmicpc.net/step)

| step | title | languages | remarks|
|:----:|-------|-----------|--------|
| 1 | [입출력과 사칙연산](https://www.acmicpc.net/step/1) | Python3 | - |
| 2 | [if문](https://www.acmicpc.net/step/4) | Python3 | - |
| 3 | [for문](https://www.acmicpc.net/step/3) | Python3 | - |
| 4 | [while문](https://www.acmicpc.net/step/2) | Python3 | - |
| 5 | [1차원 배열](https://www.acmicpc.net/step/6) | Python3 | - |
| 6 | [함수](https://www.acmicpc.net/step/5) | Python3 | - |
| 7 | [문자열](https://www.acmicpc.net/step/7) | Python3 | - |
| 8 | [기본 수학 1](https://www.acmicpc.net/step/8) | Python3 | - |
| 9 | [기본 수학 2](https://www.acmicpc.net/step/10) | Python3 | - |
| 10 | [재귀](https://www.acmicpc.net/step/19) | Python3 | - |
| ... | ... | ... | ... |
| 50 | [매우 어려운 자료구조와 알고리즘(수정 예정)](https://www.acmicpc.net/step/46) | - | - |

---
### [Programmers](https://programmers.co.kr/learn/challenges)
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
| 1 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Hash](https://programmers.co.kr/learn/courses/30/parts/12077) | - |
| 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Stack/Queue](https://programmers.co.kr/learn/courses/30/parts/12081) | - |
| 2 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Heap](https://programmers.co.kr/learn/courses/30/parts/12117) | - |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Sort](https://programmers.co.kr/learn/courses/30/parts/12198) | - |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Brute Force](https://programmers.co.kr/learn/courses/30/parts/12230) | - |
| 1 to 2 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Greedy](https://programmers.co.kr/learn/courses/30/parts/12244) | - |
| 3 to 4 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Dynamic Programming](https://programmers.co.kr/learn/courses/30/parts/12263) | - |
| 2 to 3 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [DFS/BFS](https://programmers.co.kr/learn/courses/30/parts/12421) | - |
| 3 to 4 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Binary Search](https://programmers.co.kr/learn/courses/30/parts/12486) | - |
| 3 and 5 | [Coding Test High Score Kit](https://programmers.co.kr/learn/challenges?tab=algorithm_practice_kit) | [Graph](https://programmers.co.kr/learn/courses/30/parts/14393) | - |
| no more than 5 | [모든 문제](https://programmers.co.kr/learn/challenges?tab=all_challenges) | - | - |


---
[^wiki_algorithm]: 계산의 순서로만 이해하기엔, 충분한 설명이 아닌 것 같아서 조금 더 참고한 뒤 수정하겠음.
[^wiki_structure_list]: 직군에 따라 우선적으로 파악해야 할 구조가 다를 것이기에 다음의 위키피디아 링크로 대체하나, 혹시 한국 지원이 되지 않는 링크라면 목차나 키워드만 파악 후 `Pattern`, `Flow`, 혹은 `Architecture` 등의 `Structure`와 유사한 의미를 가진 단어와 사용 언어, 목차/키워드를 조합해 검색하면 이미지 파일로 확인이 가능하다.(그 후 github 내 관심 라이브러리 소스의 `tree`를 확인하는 것도 큰 틀을 파악하기 좋은 방법이다.)
    * [Software Architecture](https://en.wikipedia.org/wiki/Software_architecture)
    * [Data Structure](https://en.wikipedia.org/wiki/Data_structure)
    * [Structure_(mathematical_logic)](https://en.wikipedia.org/wiki/Structure_(mathematical_logic))
[^wiki_logic]: 로직에 대한 내용 중 `Systems of logic`이나 `Areas of research`의 내용을 참고해서 다양한 차원에서 프로그래밍적인 고려 사항을 연결할 수 있다면 좋겠다만, 현재 나의 수준에선 Paper's Abstact 내 필수 키워드 참고 용도로만 사용 중이다.