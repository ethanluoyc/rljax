import jax.numpy as jnp
from flax import nn
from rljax.common.policy import DeterministicPolicy
from rljax.common.value import ContinuousQFunction


def build_td3_actor(state_dim, action_dim, rng_init, hidden_units=(400, 300)):
    """
    Build actor for TD3.
    """
    actor = DeterministicPolicy.partial(
        action_dim=action_dim,
        hidden_units=hidden_units,
        hidden_activation=nn.relu,
    )
    input_spec = [((1, state_dim), jnp.float32)]
    _, param_init = actor.init_by_shape(rng_init, input_spec)
    return nn.Model(actor, param_init)


def build_td3_critic(state_dim, action_dim, rng_init, hidden_units=(400, 300)):
    """
    Build critic for TD3.
    """
    critic = ContinuousQFunction.partial(
        num_critics=2,
        hidden_units=hidden_units,
        hidden_activation=nn.relu,
    )
    input_spec = [
        ((1, state_dim), jnp.float32),
        ((1, action_dim), jnp.float32),
    ]
    _, param_init = critic.init_by_shape(rng_init, input_spec)
    return nn.Model(critic, param_init)
