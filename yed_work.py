map_start = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<graphml xmlns="http://graphml.graphdrawing.org/xmlns" xmlns:java="http://www.yworks.com/xml/yfiles-common/1.0/java" xmlns:sys="http://www.yworks.com/xml/yfiles-common/markup/primitives/2.0" xmlns:x="http://www.yworks.com/xml/yfiles-common/markup/2.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:y="http://www.yworks.com/xml/graphml" xmlns:yed="http://www.yworks.com/xml/yed/3" xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns http://www.yworks.com/xml/schema/graphml/1.1/ygraphml.xsd">
  <!--Created by yEd 3.17.1-->
  <key attr.name="Description" attr.type="string" for="graph" id="d0"/>
  <key for="port" id="d1" yfiles.type="portgraphics"/>
  <key for="port" id="d2" yfiles.type="portgeometry"/>
  <key for="port" id="d3" yfiles.type="portuserdata"/>
  <key attr.name="url" attr.type="string" for="node" id="d4"/>
  <key attr.name="description" attr.type="string" for="node" id="d5"/>
  <key for="node" id="d6" yfiles.type="nodegraphics"/>
  <key for="graphml" id="d7" yfiles.type="resources"/>
  <key attr.name="url" attr.type="string" for="edge" id="d8"/>
  <key attr.name="description" attr.type="string" for="edge" id="d9"/>
  <key for="edge" id="d10" yfiles.type="edgegraphics"/>
  <graph edgedefault="directed" id="G">
"""



map_end = """</graph>
  <data key="d7">
    <y:Resources/>
  </data>
</graphml>
"""

#Name, Name Shape (rectangle)
node = """<node id="{}">
      <data key="d5"/>
      <data key="d6">
        <y:ShapeNode>
          <y:Geometry height="30.0" width="160.0" x="130.0" y="31.0"/>
          <y:Fill color="#FFCC00" transparent="false"/>
          <y:BorderStyle color="#000000" raised="false" type="line" width="1.0"/>
          <y:NodeLabel alignment="center" autoSizePolicy="content" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.701171875" horizontalTextPosition="center" iconTextGap="4" modelName="custom" textColor="#000000" verticalTextPosition="bottom" visible="true" width="25.3515625" x="2.32421875" y="5.6494140625">{}<y:LabelModel>
              <y:SmartNodeLabelModel distance="4.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartNodeLabelModelParameter labelRatioX="0.0" labelRatioY="0.0" nodeRatioX="0.0" nodeRatioY="0.0" offsetX="0.0" offsetY="0.0" upX="0.0" upY="-1.0"/>
            </y:ModelParameter>
          </y:NodeLabel>
          <y:Shape type="{}"/>
        </y:ShapeNode>
      </data>
    </node>
"""

#ID,Source, Target, description, description
link = """<edge id="e{}" source="{}" target="{}">
      <data key="d8"/>
      <data key="d9"><![CDATA[{}]]></data>
      <data key="d10">
        <y:PolyLineEdge>
          <y:Path sx="0.0" sy="0.0" tx="-14.987747979166812" ty="4.7782355959200515"/>
          <y:LineStyle color="#000000" type="line" width="1.0"/>
          <y:Arrows source="none" target="standard"/>
          <y:EdgeLabel alignment="center" configuration="AutoFlippingLabel" distance="2.0" fontFamily="Dialog" fontSize="12" fontStyle="plain" hasBackgroundColor="false" hasLineColor="false" height="18.701171875" horizontalTextPosition="center" iconTextGap="4" modelName="custom" preferredPlacement="anywhere" ratio="0.5" textColor="#000000" verticalTextPosition="bottom" visible="true" width="94.703125" x="148.8257995191616" y="179.43836906755877">{}<y:LabelModel>
              <y:SmartEdgeLabelModel autoRotationEnabled="false" defaultAngle="0.0" defaultDistance="10.0"/>
            </y:LabelModel>
            <y:ModelParameter>
              <y:SmartEdgeLabelModelParameter angle="0.0" distance="30.0" distanceToCenter="true" position="right" ratio="0.5" segment="0"/>
            </y:ModelParameter>
            <y:PreferredPlacementDescriptor angle="0.0" angleOffsetOnRightSide="0" angleReference="absolute" angleRotationOnRightSide="co" distance="-1.0" frozen="true" placement="anywhere" side="anywhere" sideReference="relative_to_edge_flow"/>
          </y:EdgeLabel>
          <y:BendStyle smoothed="false"/>
        </y:PolyLineEdge>
      </data>
    </edge>
"""