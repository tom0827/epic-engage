import React, { createContext, useState } from 'react';

export interface FileUploadContextState {
    handleAddFile: (_files: File[]) => Promise<boolean>;
    savedFileName: string;
    addedFileName: string;
    setAddedFileName: React.Dispatch<React.SetStateAction<string>>;
}

export const FileUploadContext = createContext<FileUploadContextState>({
    handleAddFile: () => {
        throw new Error('handleAddFile not implemented');
    },
    savedFileName: '',
    addedFileName: '',
    setAddedFileName: () => {
        throw new Error('setAddedFileName not implemented');
    },
});

interface FileUploadContextProviderProps {
    handleAddFile: (_files: File[]) => Promise<boolean>;
    children: React.ReactNode;
    savedFileName: string;
}
export const FileUploadContextProvider = ({
    children,
    handleAddFile,
    savedFileName,
}: FileUploadContextProviderProps) => {
    const [addedFileName, setAddedFileName] = useState('');

    return (
        <FileUploadContext.Provider
            value={{
                handleAddFile,
                savedFileName,
                addedFileName,
                setAddedFileName,
            }}
        >
            {children}
        </FileUploadContext.Provider>
    );
};
