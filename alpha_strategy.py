"""Alpha 策略生成模块"""


class AlphaStrategy:
    def get_simulation_data(self, datafields, mode=1):
        """根据模式生成策略列表"""

        if mode == 1:
            return self.generate_vec_strategy(datafields)
        elif mode == 2:
            return self.generate_matrix_strategy(datafields)
        else:
            print("❌ 无效的策略模式")
            return []

    def generate_vec_strategy(self, datafields):
        """生成vec策略"""
        strategies = []
        for field in datafields:
            strategies.extend(
                [f"my_group = market;\
my_group2 = bucket(rank(cap),range='0,1,0.1');\
alpha=rank(\
    group_rank(\
        ts_decay_linear(\
            volume/ts_sum(volume,252),10),\
            my_group)\
    *group_rank(\
        ts_rank(\
            vec_avg({field}),10),\
            my_group)\
    *group_rank(\
        -ts_delta(\
            close,5),\
            my_group));\
trade_when(volume>adv20,group_neutralize(alpha,my_group2),-1)"]
            )

        return strategies

    def generate_matrix_strategy(self, datafields):
        """生成matrix策略"""

        strategies = []
        n = len(datafields)

        for i in range(0, n-1, 2):
            field1 = datafields[i]
            field2 = datafields[i+1]

            strategies.extend([]
            )

        return strategies


