import { Cascader, Skeleton } from "antd";
import { FC, ReactNode } from "react";
import { IOperatorInfo } from "@/models/useOperatorList";
import { useModel } from "umi";

const rareLabels: string[] = [
  '★6', '★5', '★4', '★3', '★2', '★1',
];

const classLabels: string[] = [
  '近卫', '狙击', '重装', '医疗', '辅助', '术师', '特种', '先锋',
];

interface ICascadeOption {
  value: string | number;
  label?: ReactNode;
  disabled?: boolean;
  children?: ICascadeOption[];
  obj?: IOperatorInfo;
}

function cascadeOptions(operators: IOperatorInfo[]): ICascadeOption[] {
  const ret: ICascadeOption[] = rareLabels.map((rare): ICascadeOption => ({
    value: rare,
    label: rare,
    children: classLabels.map((className): ICascadeOption => ({
      value: className,
      label: className,
      children: operators.reduce((result: ICascadeOption[], operator) => {
        if (rare === rareLabels[6 - operator.rare] && className === operator.class) {
          result.push({ value: operator.name, label: operator.name, obj: operator });
        }
        return result;
      }, []),
    })),
  }));

  return ret;
}

const calcSkillNum = (opt: IOperatorInfo) => {
  if (!opt) {
    return 0;
  }

  if (opt.rare >= 6 || opt.name === '阿米娅') {
    return 3;
  }

  if (opt.rare >= 4 && opt.rare <= 5) {
    return 2;
  }

  if (opt.rare == 3) {
    return 1;
  }

  if (opt.rare <= 2) {
    return 0;
  }
};

const OperatorSelector: FC<{ setSkillNum: React.Dispatch<React.SetStateAction<number>>, flushSkills: () => void, setCharName: React.Dispatch<React.SetStateAction<string>> }> = ({ setSkillNum, flushSkills, setCharName }) => {
  const { operators, loading } = useModel('useOperatorList');

  if (loading) {
    return <Skeleton active />;
  }


  const opts = cascadeOptions(operators);

  const updateSkillNum = (opt: IOperatorInfo) => {
    setCharName(opt.name);
    flushSkills();
    setSkillNum(calcSkillNum(opt) || 0);
  };

  return <Cascader options={opts}
    placeholder="请选择干员…"
    expandTrigger="hover"
    displayRender={(label) => (label[2])}
    onChange={(_, selectedOptions) => { updateSkillNum(selectedOptions?.[2]?.obj) }}
    showSearch
  />;
};

export default OperatorSelector;
