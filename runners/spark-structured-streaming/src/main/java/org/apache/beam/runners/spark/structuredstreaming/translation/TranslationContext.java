/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package org.apache.beam.runners.spark.structuredstreaming.translation;

import java.util.HashMap;
import java.util.Map;
import org.apache.beam.runners.spark.structuredstreaming.SparkPipelineOptions;
import org.apache.beam.sdk.runners.AppliedPTransform;
import org.apache.beam.sdk.transforms.PTransform;
import org.apache.beam.sdk.values.PValue;
import org.apache.spark.SparkConf;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.SparkSession;

/**
 * Base class that gives a context for {@link PTransform} translation: keeping track of the
 * datasets, the {@link SparkSession}, the current transform being translated.
 */
public class TranslationContext {

  private AppliedPTransform<?, ?, ?> currentTransform;
  private final Map<PValue, Dataset<?>> datasets;
  private SparkSession sparkSession;
  private final SparkPipelineOptions options;

  public void setCurrentTransform(AppliedPTransform<?, ?, ?> currentTransform) {
    this.currentTransform = currentTransform;
  }

  public TranslationContext(SparkPipelineOptions options) {
    SparkConf sparkConf = new SparkConf();
    sparkConf.setMaster(options.getSparkMaster());
    sparkConf.setAppName(options.getAppName());
    if (options.getFilesToStage() != null && !options.getFilesToStage().isEmpty()) {
      sparkConf.setJars(options.getFilesToStage().toArray(new String[0]));
    }

    this.sparkSession = SparkSession.builder().config(sparkConf).getOrCreate();
    this.options = options;
    this.datasets = new HashMap<>();
  }
}