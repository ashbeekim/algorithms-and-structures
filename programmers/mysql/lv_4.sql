-- 우유와 요거트가 담긴 장바구니

-- 입양 시각 구하기(2)
SET @HOUR_RANGE = -1;
SELECT  (@HOUR_RANGE := @HOUR_RANGE + 1) AS 'Hour',
    (SELECT COUNT(*) FROM animal_outs WHERE HOUR(datetime) = @HOUR_RANGE) AS 'Count'
FROM animal_outs
WHERE @HOUR_RANGE < 23;       

-- 보호소에서 중성화한 동물
SELECT outs.animal_id, outs.animal_type, outs.name
FROM animal_outs outs 
LEFT JOIN animal_ins ins 
    ON outs.animal_id = ins.animal_id
    AND outs.sex_upon_outcome <> ins.sex_upon_intake
WHERE ins.sex_upon_intake IS NOT NULL
ORDER BY outs.animal_id;


/*
이쯤에서 뭔가 SQL 고득점 Kit와 모든 문제는 다른 기준을 가지고 있음을 확신함.

"보호소에서 중성화한 동물" 구조 당시 중성화 전이었던 아이들 중 입양된 아이들을 중성화했다면, 입양된 테이블에서 조회하는 게 더 빠른 결과를 도출할 것이란 생각에 위와 같이 작성함.
처음엔 NULL값을 고려하지 못 하고 제출했는데, 틀렸대서 select에 값을 추가해서 확인해보니 데이터 누락에 대한 처리를 해야함을 알 수 있었음.

남은 문제는 이번 주 내로 업데이트 할 예정임.
현재 기준으로 level 5는 MySQL, Oracle 모두 없음.
*/
