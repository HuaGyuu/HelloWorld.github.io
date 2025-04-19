extends Control

# 文本数组
var texts = [
	"Hello World",       # 英语
	"你好世界",          # 中文简体
	"こんにちは世界",    # 日语
	"안녕 세상",         # 韩语
	"Hola Mundo",       # 西班牙语
	"Bonjour le monde", # 法语
	"Hallo Welt",       # 德语
	"Ciao mondo",       # 意大利语
	"Привет мир",       # 俄语
	"Olá Mundo",        # 葡萄牙语
	"مرحبا بالعالم",    # 阿拉伯语
	"नमस्ते दुनिया",    # 印地语
	"สวัสดีชาวโลก",      # 泰语
	"Xin chào thế giới", # 越南语
	"Hej världen",      # 瑞典语
	"Hallo Wereld",     # 荷兰语
	"Witaj świecie",    # 波兰语
	"Γειά σου Κόσμε",   # 希腊语
	"Merhaba Dünya",    # 土耳其语
	"Hej Verden",       # 丹麦语
	"Halló heimur",     # 冰岛语
	"سلام دنیا",        # 波斯语
	"Kamusta Mundo"     # 菲律宾语
]

# 生成文本的计时器
var spawn_timer = 0
var spawn_interval = 0.5 # 每0.5秒生成一个文本

func _ready():
	# 设置随机种子
	randomize()

func _process(delta):
	spawn_timer += delta
	if spawn_timer >= spawn_interval:
		spawn_timer = 0
		spawn_text()

func spawn_text():
	# 创建新的Label节点
	var label = Label.new()
	
	# 设置文本属性
	label.text = texts[randi() % texts.size()]
	
	# 随机位置
	var screen_size = get_viewport_rect().size
	label.position = Vector2(
		randf_range(0, screen_size.x),
		randf_range(0, screen_size.y)
	)
	
	# 添加到场景
	add_child(label)
	
	# 设置动画
	var tween = create_tween()
	tween.tween_property(label, "modulate:a", 0.0, 2.0)
	tween.tween_callback(label.queue_free)
