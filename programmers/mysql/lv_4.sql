-- 우유와 요거트가 담긴 장바구니

-- 입양 시각 구하기(2)
SET @HOUR_RANGE = -1;
SELECT  (@HOUR_RANGE := @HOUR_RANGE + 1) AS 'Hour',
    (SELECT COUNT(*) FROM animal_outs WHERE HOUR(datetime) = @HOUR_RANGE) AS 'Count'
FROM animal_outs
WHERE @HOUR_RANGE < 23;

-- 보호소에서 중성화한 동물

/*
이쯤에서 뭔가 SQL 고득점 Kit와 모든 문제는 다른 기준을 가지고 있음을 확신함.
남은 문제는 이번 주 내로 업데이트 할 예정임.
현재 기준으로 level 5는 MySQL, Oracle 모두 없음.
*/