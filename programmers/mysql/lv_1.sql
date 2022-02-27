-- 모든 레코드 조회하기
SELECT *
FROM ANIMAL_INS
ORDER BY ANIMAL_ID;

-- 최댓값 구하기
SELECT MAX(datetime) FROM animal_ins;

-- 이름이 없는 동물의 아아디
SELECT animal_id FROM animal_ins
WHERE name IS NULL;

-- 역순 정렬하기
SELECT name, datetime
FROM animal_ins
ORDER BY animal_id desc;

-- 이름이 있는 동물의 아이디
SELECT animal_id FROM animal_ins
WHERE name IS NOT NULL;

-- 아픈 동물 찾기
SELECT animal_id, name
FROM animal_ins
WHERE intake_condition = 'Sick'
ORDER BY animal_id;

-- 어린 동물 찾기
SELECT animal_id, name 
FROM animal_ins
WHERE intake_condition NOT LIKE '%Aged%'
ORDER BY animal_id;

-- 동물의 아이디와 이름
SELECT animal_id, name
FROM animal_ins
ORDER BY animal_id;

--여러 기준으로 정렬하기
SELECT animal_id, name, datetime
FROM animal_ins
ORDER BY name,
    datetime desc;

-- 상위 n개 레코드
SELECT name FROM (
  SELECT name, RANK() OVER (ORDER BY datetime) AS dt_rank FROM animal_ins
) animal_rank
WHERE dt_rank = 1;

/*
level 1은 SQL 기초 중에서도 읽기만 알면 쉽게 결과 제출이 가능함
모든 문제에서 level 1에 MySQL을 선택하면 위의 순서로 나오는데, 필터 설정 이후에 어떤 기준으로 정렬한 사이트인지 궁금해짐
언어 선택에 대한 이미지 매핑이 이상하게 된 건가? 그게 아니면 어떤 요인때문에 그러한가? 하는 호기심이 들었지만 어디서 적용이 이뤄지는가에서 생각을 멈춤

basic)
작성: SELECT>FROM>WHERE>GROUP BY>HAVING>ORDER BY
처리: FROM>WHERE>GROUP BY>HAVING>SELECT>ORDER BY
*/