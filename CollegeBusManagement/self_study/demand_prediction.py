"""Optional sample-only bus demand prediction; not used by the core application."""


def predict_demand(sample_days: int = 4) -> float:
    try:
        import numpy as np
        from sklearn.linear_model import LinearRegression
    except ImportError as exc:
        raise RuntimeError("Install the optional packages with: pip install numpy scikit-learn") from exc
    if sample_days < 1:
        raise ValueError("sample_days must be positive.")
    days = np.array([[1], [2], [3], [4], [5]], dtype=float)
    riders = np.array([82, 88, 85, 96, 101], dtype=float)
    model = LinearRegression().fit(days, riders)
    return float(model.predict(np.array([[sample_days]], dtype=float))[0])


if __name__ == "__main__":
    print(f"Approximate riders for day 6: {predict_demand(6):.1f}")
