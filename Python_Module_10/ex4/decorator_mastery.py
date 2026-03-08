import time
import functools

def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power_level = kwargs.get('power')
            if power_level is None:
                for arg in args:
                    if isinstance(arg, int):
                        power_level = arg
                        break
            if power_level is None or power_level < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper

    return decorator

    
def retry_spell(max_attempts: int) -> callable:

    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")
            
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper

    return decorator

    
class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True


    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def main():
    print("Testing spell timer...")
    
    @spell_timer
    def fireball():
        time.sleep(0.1) 
        return "Fireball cast!"
        
    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    
    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("X"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()


