-- 고양이와 개는 몇 마리 있을까
SELECT animal_type, COUNT(1) FROM animal_ins
WHERE animal_type = 'Cat' OR animal_type = 'Dog'
GROUP BY animal_type
ORDER BY animal_type;

-- 루시와 엘라 찾기
SELECT animal_id, name, sex_upon_intake
FROM animal_ins
WHERE name IN ('Lucy','Ella','Pickle','Rogan','Sabrina','Mitty')
ORDER BY animal_id;

-- 최솟값 구하기
SELECT MIN(datetime) FROM animal_ins;

-- 동명 동물 수 찾기
SELECT name, count(name) AS count FROM animal_ins
GROUP BY name
HAVING count >= 2
ORDER BY name;

-- 이름에 el이 들어가는 동물 찾기
SELECT animal_id, name
FROM animal_ins
WHERE animal_type = "Dog" AND name LIKE '%el%'
ORDER BY name;

-- 동물 수 구하기
SELECT COUNT(1) FROM animal_ins;

-- 입양 시각 구하기(1)
SELECT HOUR(datetime), count(1) FROM animal_outs
WHERE DATE_FORMAT(datetime, '%H:%i') BETWEEN '09:00' AND '19:59'
GROUP BY HOUR(datetime)
ORDER BY HOUR(datetime);

-- NULL 처리하기
SELECT animal_type, IFNULL(name, "No name") AS name, sex_upon_intake FROM animal_ins;

-- 중성화 여부 파악하기
SELECT animal_id, name, 
    IF(LEFT(sex_upon_intake, 6) IN ("Neuter", "Spayed"), "O", "X") as "중성화"
FROM animal_ins
ORDER BY animal_id;

-- 중복 제거하기
SELECT COUNT(DISTINCT name) FROM animal_ins;

-- DATETIME에서 DATE로 형 변환
SELECT animal_id, name,
    DATE_FORMAT(datetime, "%Y-%m-%d") AS "날짜"
FROM animal_ins
ORDER BY animal_id;

/*
MAX, MIN이 level1, level 2로 나뉘는 건 아직도 이유를 모르겠음.
"루시와 엘라 찾기"를 CONCAT으로 작성한 분이 계셔서, STRING_SPLIT으로 풀어보려는 시도를 했으나 실패함.

DATE_FORMAT은 MySQL 공식 문서에서 참고하는 게 제일 빠름.
*/