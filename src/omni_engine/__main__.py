from omni_engine.core import SuperEngineOmniCore7Master


def main():
    engine = SuperEngineOmniCore7Master()
    engine.initialize_state([1.0, 1.5, 2.0, 2.5])
    result = engine.execute_evolution_cycle("ziolkowski")
    print(result)


if __name__ == "__main__":
    main()
