-- 없어진 기록 찾기
SELECT outs.animal_id, outs.name
FROM animal_ins ins 
RIGHT JOIN animal_outs outs 
    ON ins.animal_id = outs.animal_id
WHERE ins.animal_id IS NULL
ORDER BY outs.animal_id;

-- 있었는데요 없었습니다
SELECT outs.animal_id, outs.name
FROM animal_ins ins 
RIGHT JOIN animal_outs outs 
    ON ins.animal_id = outs.animal_id
WHERE TIMEDIFF(ins.datetime, outs.datetime) > 0
ORDER BY ins.datetime;

-- 오랜 기간 보호한 동물(1)
SELECT ins.name, ins.datetime
FROM animal_ins ins 
LEFT JOIN animal_outs outs 
    ON ins.animal_id = outs.animal_id
WHERE outs.animal_id IS NULL
ORDER BY ins.datetime
LIMIT 3;

-- 헤비 유저가 소유한 장소

-- 오랜 기간 보호한 동물(2)
SELECT outs.animal_id AS animal_id, 
    outs.name AS name
FROM animal_ins ins 
RIGHT JOIN animal_outs outs 
    ON ins.animal_id = outs.animal_id
ORDER BY TIMESTAMPDIFF(DAY, ins.datetime, outs.datetime) desc
LIMIT 2;

/*
"오랜 기간 보호한 동물(2)"에서 ORDER BY TIMEDIFF(ins.datetime, outs.datetime) desc로 출력했다가 여러 "838:59:59" 값 반환으로 정답이 아니라는 결과에 join에서 실수한 것이란 생각을 했음
근데 입양을 가야 일자를 산출할 수 있을테니, 다른 원인을 찾아봄. TIMEDIFF는 60일까지만 시분초로 반환한다고 함. 따라서 일자로 반환되도록 TIMESTAMPDIFF(DAY, ins.datetime, outs.datetime) 사용.
*/