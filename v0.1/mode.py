#this file documents the spec of different dungeon modes
layoutdict = {
    # 
    0:
    {
        "segments_x":3,
        "segments_y":2,
        "chances_for_dummy":[[0.1,0.1,0.1],[0.1,0.1,0.1]],
        "duplicated chance":0.2
    },
    1:
    {
        "segments_x":4,
        "segments_y":3,
        "chances_for_dummy":[[0,0,0,0],[0,1,1,0],[0,0,0,0]],
        "duplicated chance":0.4
    },
    2:
    {
        "segments_x":6,
        "segments_y":5,
        "chances_for_dummy":[[0.3,0.3,0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3,0.3,0.3],[0.3,0.3,0.3,0.3,0.3,0.3]],
        "duplicated chance":0.4
    }
}