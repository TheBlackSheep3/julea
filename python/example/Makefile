run:
	../../scripts/setup.sh start
	python hello-world.py
	../../scripts/setup.sh stop

check-py:
	../../scripts/setup.sh start
	python read.py
	../../scripts/setup.sh stop

clean:
	$(RM) checker write
	../../scripts/setup.sh stop
	../../scripts/setup.sh clean
