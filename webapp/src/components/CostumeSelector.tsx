import { Select, Skeleton } from "antd";
import { FC } from "react";
import { useModel } from "umi";

const CostumeSelector: FC<{ charName: string }> = ({ charName }) => {
  const { costumes, loading } = useModel('useCostumeList');

  if (loading) {
    return <Skeleton active />;
  }

  const charCostumes = costumes.filter(costume => costume.owner === charName);

  return (
    <Select style={{ width: 175 }}>
      <Select.Option value="1">初始</Select.Option>
      <Select.Option value="2">精英2</Select.Option>
      {
        charCostumes.map(costume =>(
          <Select.Option value={costume.code}>{`${costume.series} - ${costume.name}`}</Select.Option>
        ))
      }
    </Select>
  );
};

export default CostumeSelector;
