candle_box_contains = 0
candle_box = 0
total_boxes = 0

for i in range(101):
    
    while i > candle_box_contains:
        candle_box_contains += 24
        candle_box += 1
    if candle_box != 0:  
        total_boxes += candle_box   
        print(f"Before birthday {i}, buy {candle_box} box(es)")
    candle_box_contains -= i
    candle_box = 0
print(f"Total number of boxes: {total_boxes}, Remaining candles: {candle_box_contains}")
    