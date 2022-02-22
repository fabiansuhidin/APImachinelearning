from tensorflow_datasets.image_classification import food101
import tensorflow_datasets.testing as tfds_test


class Food101Test(tfds_test.DatasetBuilderTestCase):
  DATASET_CLASS = food101.Food101
  SPLITS = {
      "train": 4,
      "validation": 4,
  }


if __name__ == "__main__":
  tfds_test.test_main()
